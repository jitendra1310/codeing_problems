const router = require('express').Router();
const User = require('../model/User')
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
//validation
const Joi = require('@hapi/joi');

/* const schema = {
    name: Joi.string().min(6).required(),
    email: Joi.string().min(6).required().email(),
    password: Joi.string().min(6).required()
} */


router.post("/register",async(req,res)=>{
    
    try{
        // Lets validate date before We Make User
        //const {validate_error} = Joi.validate(req.body,schema);

        //checking if user already in database
        const emailExist = await User.findOne({email:req.body.email});
        if(emailExist) return res.status(400).send('Email Allready Exist!'); 

        //Hash password
        const salt = await bcrypt.genSalt(10);
        const hashedPassword = await bcrypt.hash(req.body.password,salt);

        //creating a new user
        const user = new User({
            name: req.body.name,
            email: req.body.email,
            password:hashedPassword 
        });
        const userSaved = await user.save();
        console.log(userSaved);
        res.send(userSaved);            

    }catch(err1){
        res.status(400).send(err1)
    }
});

//LOGIN

router.post('/login',async(req,res)=>{
    
    //checking if user email exist
    const user = await User.findOne({email:req.body.email});
    if(!user) return res.status(400).send('Email is not found!'); 

    //Paaword is Correct
    const vaildPass = await bcrypt.compare(req.body.password,user.password)
    if(!vaildPass) return res.status(400).send('Invaild password');

    //create and assign a token
    const token = jwt.sign({_id:user._id},process.env.TOKEN_SECERT);
    res.header('auth-token',token).send(token);
    res.send('Logged In');

});

module.exports = router; 
 