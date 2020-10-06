const router = require('express').Router();
const verify = require('./varifyToken')
router.get('/',verify,(req,res) =>{
 res
    res.json({
        posts:{
            title: 'My Fisrst Post',
            description : 'My Fisrst Post Description'
        }
    });

});

module.exports = router; 