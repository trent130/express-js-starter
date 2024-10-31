const express =  require('express');
const mongoose = require('mongoose');
const app = express();



app.get('/',  (req, res) => {
    res.send("Hello from the node api server");
})

app.post('api/products', (req, res)=> {
    console.log(req.body)
    res.send("data reserved")
})

mongoose.connect("mongodb+srv://lawrencewafula408:CfOeaCu20a1gUsh4@backend.pq28j.mongodb.net/Backend?retryWrites=true&w=majority&appName=Backend")
.then(() => {
    console.log("connected to database")
    const port = 3000;
    app.listen(port, ()=> {
        console.log('server is running on port 3000')
    });
})

.catch( () => {
    console.log("error connecting to database")
})

