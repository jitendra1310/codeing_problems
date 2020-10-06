const express = require('express'); 
const app = express();
const mongoose = require('mongoose');
const dotenv = require('dotenv');
//const bodyParser = require('body-parser')

//Import Routes
const authRoute = require('./routes/auth');
const postRoute = require('./routes/posts')

dotenv.config();

//DB Connect  || process.env.DB_CONNECT,
//console.log(process.env);

mongoose.connect(
    process.env.DB_CONNECT,      
    {
        useUnifiedTopology: true,
        useNewUrlParser: true 
    },    
    () => console.log('connected to db')
);

//Middelware
app.use(express.json());
//app.use(bodyParser.json());

// Route Middelwares
app.use('/api/user',authRoute);
app.use('/api/posts',postRoute);

app.listen(3001,() => console.log('Server up and running on port : 3001'));
