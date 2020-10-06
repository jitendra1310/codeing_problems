const jwt = require('jsonwebtoken');

module.exports = function(req,res,next) {
    const token = req.header('auth-token');
    if(!token) return res.status(401).send('Access Deined!');
    
    try{
        const varified = jwt.varified(token,process.env.TOKEN_SECERT);
        req.user = varified;
        next();
    }catch(err){
        res.status(400).send('Invalid token');

    }
}