<?php

/*
 * @auther : 
 * @description : clean the old features  
 * and open the template in the editor.
 */
ini_set("display_errors", "-1");
error_reporting(E_ALL);
set_time_limit(0);
define('AREA', 'A');
define('AREA_NAME', 'admin');
require_once dirname(__FILE__) . './../prepare.php';
require_once dirname(__FILE__) . './../init.php';
require_once DIR_CORE . 'DBOperations.php';
require_once DIR_CORE . 'class.catalog_process.php';
$db = new DBOperations();
$debug = (isset($_REQUEST['debug'])) ? 1 : 0;
define('DEBUG', $debug);
$requestArr = $_REQUEST;
$instanceArray = getInstanceInfo($requestArr);
if(empty($instanceArray['product_id']));
    define('DEBUG', 0);    

    try {
        if($instanceArray['product_id_execution_start'] < $instanceArray['product_id_execution_end']){            
            $cronInfo['cron_key'] = $instanceArray['cron_key'];            
            $productsData = $db->dbGetArray($instanceArray['query']);         
            if(!empty($productsData)){
            foreach ($productsData as $productsValue) {
                   $productId = $productsValue['product_id'];
                   $cronInfo['cron_value'] = $productId;                
                   featutesCleanup($productId, $cronInfo); 
               }
               if(empty($instanceArray['product_id']))
                    fn_catalog_cron_execution_update($cronInfo);
               
            }elseif($requestArr['product_id']==''){
                $executedIds = $instanceArray['product_id_execution_start']+$instanceArray['limit'] ;              
                $cronInfo['cron_value'] = ($executedIds<=$instanceArray['product_id_execution_end'])?$executedIds:$instanceArray['product_id_execution_end'];
                fn_catalog_cron_execution_update($cronInfo);
            }
        } 
    } catch (Exception $exc) {
        echo $exc->getTraceAsString();
    }


echo "done";


function featutesCleanup($productID, $cronInfo) {
    if (DEBUG == 1) {
        echo "<br/><pre><b>METHOD NAME:" . __METHOD__ . " Product ID:</b>";
        print_r($productID);
    }
    if (!empty($productID)) {
        try {
            $categoryId = getProductMainCategoryId($productID);
            $productCategoryFeatures = getProductCategoryFeatures($categoryId);
            fnDebug($productCategoryFeatures, 'Product Taged Features');
            $productUnusedFeatures = getUnusedProductFeatures($productCategoryFeatures, $productID);
            if (!empty($productUnusedFeatures)) {
                backupOldFeatures($productUnusedFeatures);
                fn_product_update($productID);
            }
            
        } catch (Exception $exc) {
            echo $exc->getTraceAsString();
        }
    }
}

function getUnusedProductFeatures($productCategoryFeatures, $productID) {
    if (DEBUG == 1) {
        echo "<br/><pre><b>METHOD NAME:" . __METHOD__ . " Product Category Features:</b>";
        print_r($productCategoryFeatures);
    }
    try {
        if (!empty($productCategoryFeatures)) {
            $db = new DBOperations();
            $sql = "select product_id,feature_id,variant_id,value,value_int,lang_code from cscart_product_features_values 
           where product_id='$productID' and feature_id not in ($productCategoryFeatures)";
            fnDebug($sql, "Get Unused Product Features");
            $result = $db->dbGetArray($sql);
            fnDebug($result, "Get Unused Product Features");
            $result = (!empty($result))?$result:array(); 
            return $result;
        }
    } catch (Exception $exc) {
        echo $exc->getTraceAsString();
    }
}

function getProductCategoryFeatures($categoryId) {
    if (DEBUG == 1) {
        echo "<br/><pre><b>METHOD NAME:" . __METHOD__ . " categoryId:</b>";
        print_r($categoryId);
    }
    $catalogProcessObj = new catalogProcess();
    $productCategoryFeatures = $catalogProcessObj->fn_get_product_features_category_wise($categoryId, 1);
    $productCategoryFeatures = array_keys($productCategoryFeatures);
    $productCategoryFeatures = implode(',', $productCategoryFeatures);
    fnDebug($productCategoryFeatures, "Get Product Category Features");
    return $productCategoryFeatures;
}

function getProductMainCategoryId($productID) {
    if (DEBUG == 1) {
        echo "<br/><pre><b>METHOD NAME:" . __METHOD__ . " productID:</b>";
        print_r($productID);
    }
    try {
        $db = new DBOperations();
        $sql = "select cpc.category_id from cscart_products cp inner join 
                    cscart_products_categories cpc on cpc.product_id=cp.product_id 
                    where cpc.link_type='M' AND cp.product_id='$productID'";
        fnDebug($sql, 'Query For ProductMainCategoryId');
        $result = $db->dbGetField($sql);
        fnDebug($categoryId, "Result of Product Main Category Id");
        $result = (!empty($result))?$result:0; 
        return $result;
    } catch (Exception $exc) {
        throwException($exc);
    }
}

/* backupOldFeatures 
 * Insert product removed Features 
 * Array $productRemovedFeatures 
 */

function backupOldFeatures($productRemovedFeatures) {
    if (DEBUG == 1) {
        echo "<br/><pre><b>METHOD NAME:" . __METHOD__ . " product Removed Features:</b>";
        print_r($productRemovedFeatures);
    }
    try {
        if (!empty($productRemovedFeatures)) {
            $db = new DBOperations();

            foreach ($productRemovedFeatures as $productRemovedFeaturesValues) {
                $backup_sql = "INSERT INTO `clues_deleted_product_features_values` (`feature_id`,`product_id`,`variant_id`,`value`,`value_int`,`lang_code`,`deletd_time`) VALUES "
                        . "('$productRemovedFeaturesValues[feature_id]',"
                        . "'$productRemovedFeaturesValues[product_id]',"
                        . "'$productRemovedFeaturesValues[variant_id]',"
                        . '"'.mysql_real_escape_string($productRemovedFeaturesValues['value']).'",'
                        . "'$productRemovedFeaturesValues[value_int]',"
                        . "'$productRemovedFeaturesValues[lang_code]',"
                        . "NOW())";
                fnDebug($backup_sql, "Backup Features");
                if (db_query($backup_sql)) {
                    $delete_sql = "DELETE FROM cscart_product_features_values WHERE "
                            . "product_id='$productRemovedFeaturesValues[product_id]' AND "
                            . "feature_id ='$productRemovedFeaturesValues[feature_id]' AND "
                            . "variant_id ='$productRemovedFeaturesValues[variant_id]' AND "
                            . "lang_code='$productRemovedFeaturesValues[lang_code]'";

                    if ($productRemovedFeaturesValues['value'] == '')
                        $delete_sql .=" AND value=''";
                    elseif ($productRemovedFeaturesValues['value'] == 0)
                        $delete_sql .=" AND value='0'";
                    elseif (is_null($productRemovedFeaturesValues['value']))
                        $delete_sql .=" AND value is null";
                    else
                        $delete_sql .=' AND value="'.mysql_real_escape_string($productRemovedFeaturesValues['value']).'"';

                    if ($productRemovedFeaturesValues['value_int'] == '')
                        $delete_sql .=" AND value_int is null";
                    elseif ($productRemovedFeaturesValues['value_int'] == 0)
                        $delete_sql .=" AND value_int='0'";
                    else
                        $delete_sql .=" AND value_int='$productRemovedFeaturesValues[value_int]'";                   
                            
                    fnDebug($delete_sql, "Deleted Features");
                    db_query($delete_sql); //Delete
                }
            }
        }
    } catch (Exception $exc) {
        throwException($exc);
    }
}

function fn_catalog_cron_execution($cronInfo) {
    if (DEBUG == 1) {
        echo "<br/><pre><b>METHOD NAME:" . __METHOD__ . " Cron Info:</b>";
        print_r($cronInfo);
    }
    $sql = "INSERT INTO `clues_catalog_cron_execution` (`id`,`cron_key`,`cron_value`,`last_update_dt`) VALUES "
            . "('',"
            . "'$cronInfo[cron_key]',"
            . "'$cronInfo[cron_value]',"
            . "NOW())";
    fnDebug($sql, "cron execution");
    db_query($sql);
}

function fnDebug($arrayInfo, $title = '') {
    if (DEBUG == 1) {
        $Title = ($title == '') ? '' : $title . '<br/>';
        echo "<br/><pre><b>$Title</b>";
        print_r($arrayInfo);
        echo "<br/>";
    }
}
function getInstanceInfo($requestArr){
    if (DEBUG == 1) {
        echo "<br/><pre><b>METHOD NAME:" . __METHOD__ . " Get Instance Info:</b>";
        print_r($requestArr);
    }
    $db             = new DBOperations();
    $product_id     = '';
    $instance       = (isset($requestArr['instance']) && $requestArr['instance'] > 0)?(int)$requestArr['instance']:1;
    $limit          = (isset($requestArr['limit']) && $requestArr['limit'] > 0)?(int)$requestArr['limit']:1000;
    $max_limit      = (isset($requestArr['max_limit'])) ? $requestArr['max_limit'] : 5000000;
    $mode           = (isset($requestArr['mode']) && $requestArr['mode'] > 0)?(int)$requestArr['mode']:1;    
    $time_interval  = (isset($requestArr['t_interval'])) ? $requestArr['t_interval'] : 2;
    $catFrom        = (isset($requestArr['cat_from'])) ? $requestArr['cat_from'] : 0;
    $catTo          = (isset($requestArr['cat_to'])) ? $requestArr['cat_to'] : 0;
    
    $query          = "select cp.product_id,cpc.category_id,cp.`status` from cscart_products cp 
inner join cscart_products_categories cpc on cpc.product_id=cp.product_id 
where cpc.link_type='M'";
   
    /********************** Manage Instance Info ********************/
    $instanceArray = array('instance' => 'Instance'.$instance,
        'product_id_execution_start' => ($instance-1)*$max_limit,
        'product_id_execution_end' => $instance*$max_limit,
        'limit' => $limit,
        'product_id'=>$product_id );
    
    
   if($mode==1){
     /*************************** For All products ********************/
     $cron_key = "product_features_cleanup_cron_".$instanceArray['instance'];
     
    } elseif($mode==2 && isset($requestArr['product_id'])){
     /*************************** For Singel product_id ********************/
        $cron_key = '';        
        $product_id = (int)$requestArr['product_id'];
        $instanceArray['product_id']= $product_id;
    }elseif($mode==3){ 
     /*************************** For Time Interval ********************/   
     $cron_key = "product_features_daily_cleanup_cron_".date('d-m-Y')."_".$time_interval."_".$instanceArray['instance'];  
    
    }elseif($mode==4){ 
     /*************************** For CategoryIds ********************/   
     $cron_key = "product_features_cleanup_by_categoryIds_cron_catFrom_".$catFrom."_catTo_".$catTo."_".$instanceArray['instance'];  
    }
     
     $instanceArray['cron_key'] = $cron_key;
     $cronInfo['cron_key']=$cron_key;
     
    if($cron_key!=''){ 
        $executionInfo = get_catalog_cron_execution_info($cronInfo); 
        if(!empty($executionInfo)){
            $instanceArray['cron_id'] = $executionInfo['id'];
            $instanceArray['product_id_execution_start']=$executionInfo['cron_value'];            
        }else{   
            $cronInfo['cron_value']=$instanceArray['product_id_execution_start'];
            fn_catalog_cron_execution($cronInfo);
            $executionInfo = get_catalog_cron_execution_info($cronInfo);
            $instanceArray['cron_id'] = $executionInfo['id'];
        }
       
    }
     /********************** Manage Mode ********************/
    if($product_id!='' && $mode==2){
        $query .=" and cp.product_id='$product_id' ";
    }elseif($mode==3){
         $max_array = array('mode'=>$mode,'time_interval'=>$time_interval);               
         $instanceArray['product_id_execution_end'] = getMaxPid($max_array);         
         $query .=" AND cp.last_update > DATE_SUB(CURDATE(), INTERVAL $time_interval DAY) AND cp.product_id > $instanceArray[product_id_execution_start] AND cp.product_id < $instanceArray[product_id_execution_end] ORDER BY cp.product_id ASC limit 0,$instanceArray[limit]";        
    }elseif($mode==4){ 
         $max_array = array('catTo'=>$catTo,'catFrom'=>$catFrom,'mode'=>$mode);             
         $instanceArray['product_id_execution_end'] = getMaxPid($max_array); 
        $query .=" and cpc.category_id >= $catFrom and cpc.category_id <=$catTo  and cp.product_id > $instanceArray[product_id_execution_start] and cp.product_id < $instanceArray[product_id_execution_end] ORDER BY cp.product_id ASC limit 0,$instanceArray[limit]";        
    }
    else{        
         $query .=" and cp.product_id > $instanceArray[product_id_execution_start] and cp.product_id < $instanceArray[product_id_execution_end] ORDER BY cp.product_id ASC limit 0,$instanceArray[limit]";        
   }
     /********************** End Manage Mode ********************/ 
        $instanceArray['query'] = $query;   
        fnDebug($instanceArray, "Instance Info");
    return $instanceArray;
    
}

function fn_catalog_cron_execution_update($cronInfo) {
    if (DEBUG == 1) {
        echo "<br/><pre><b>METHOD NAME:" . __METHOD__ . " Cron Info:</b>";
        print_r($cronInfo);
    }
    $db             = new DBOperations();
    $sql = "UPDATE `clues_catalog_cron_execution` SET`cron_value`='$cronInfo[cron_value]', `last_update_dt`=NOW() WHERE `cron_key`='$cronInfo[cron_key]'";
      
    fnDebug($sql, "cron execution update");
    db_query($sql);
}

function get_catalog_cron_execution_info($cronInfo) {
    if (DEBUG == 1) {
        echo "<br/><pre><b>METHOD NAME:" . __METHOD__ . " Cron Info:</b>";
        print_r($cronInfo);
    }
     $db             = new DBOperations();     
     $sql = "select cron_value,id,cron_key from clues_catalog_cron_execution where cron_key='$cronInfo[cron_key]'";        
     fnDebug($sql, "Get Execution Info Query");
     $result = $db->dbGetArray($sql);
     $result = (!empty($result))?$result[0]:array();     
     fnDebug($result, "Get Execution data");     
    return $result;
}

function getMaxPid($array) {
    if (DEBUG == 1) {
        echo "<br/><pre><b>METHOD NAME:" . __METHOD__ . " Get Max Pid:</b>";
        print_r($array);
    }
     $db             = new DBOperations();
     if($array['mode']==3 || $array['mode']==4 ){
        if($array['mode']==3){
            $countQuery = "select cp.product_id from cscart_products cp inner join "
                    . "cscart_products_categories cpc on cpc.product_id=cp.product_id where cpc.link_type='M' "
                    . "AND cp.last_update > DATE_SUB(CURDATE(), INTERVAL $array[time_interval] DAY) order by cp.product_id desc limit 1";      
        }elseif ($array['mode']==4) {
             $countQuery = "select cp.product_id from cscart_products cp inner join "
                     . "cscart_products_categories cpc on cpc.product_id=cp.product_id where "
                     . "cpc.link_type='M' and cpc.category_id >= $array[catFrom] and cpc.category_id <=$array[catTo] order by cp.product_id desc limit 1";   
           
       }
       fnDebug($countQuery, "Get Max Pid Query");
       $result = $db->dbGetField($countQuery); 
       fnDebug($result, "Get Max Pid");
       $result = (!empty($result))?$result:0; 
     }   
        
    return $result;
}
function fn_product_update($product_id) {
    if (DEBUG == 1) {
        echo "<br/><pre><b>METHOD NAME:" . __METHOD__ . " Cron Info:</b>";
        print_r($cronInfo);
    }
    if(!empty($product_id)){
        $db             = new DBOperations();
    $sql = "UPDATE `cscart_products` SET`last_update`=NOW() WHERE `product_id`=$product_id";
      
    fnDebug($sql, "cron execution update");
    db_query($sql);
    }
    
}
