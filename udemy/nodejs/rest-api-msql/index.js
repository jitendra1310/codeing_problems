const express = require('express');
const mysql = require('mysql');
//Request Parsar
const bodyParser = require('body-parser');
//Valiadte Input
//const { check, validationResult } = require('express-validator');

//http Server setup
var app = express();
//Request and response dataformat
app.use(bodyParser.json());
//

//Mysql Database Connection string
var mysqlConnection = mysql.createConnection({
    host:'localhost',
    user: 'root',
    password: 'password',
    database: 'Library'
});

mysqlConnection.connect((err) => {
    if(!err){
        console.log("Mysql DB Connected Sucessfully!!!");        
    }else{
        console.log("Mysql DB Connection failed \n Error :"+json.stringify(err,undefined,2));
    }
});

/*Routes***/ 

//Get All  the books
app.get('/books',(req,res)=>{
    mysqlConnection.query("SELECT * FROM books",(error,rows,fields)=>{
        var result = {
            status:true,
            data:{},
            msg:""
        }
        if(!error){
            result.data = rows;
            console.log(result);
            res.send(result);
        }else{
            console.log(error);
        }
    });
});

//Get book
app.get('/books/:book_id',(req,res)=>{
    mysqlConnection.query("SELECT * FROM books where book_id=?",[req.params.book_id],(error,rows,fields)=>{
        var result = {
            status:true,
            data:{},
            msg:""
        }
        if(!error){
            result.data = rows;
            console.log(result);
            res.send(result);
        }else{
            console.log(error);
        }
    });
});

//Delete The book
app.get('/books/:book_id',(req,res)=>{
    mysqlConnection.query("DELETE FROM books where book_id=?",[req.params.book_id],(error,rows,fields)=>{
        var result = {
            status:true,
            data:{},
            msg:""
        }
        if(!error){
            let message = "Deleted successfully!!!";
            result.msg = message;
            res.send(result);
            console.log(result);            
        }else{
            console.log(error);
        }
    });
});

//Add The book
app.post('/books',(req,res)=>{
    let request_books = req.body;
    res.send(request_books);
    console.log(req);
            
});


//Start Server
app.listen(9009,()=>{
   console.log("Express server in running on port no:9009");  
});