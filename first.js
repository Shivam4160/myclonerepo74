const express =  require('express');
const app = express();
const path = require('path');
const PORT = 6000;

app.get ('/' , (req,res) => {
    // res.send('<h1> Hello! world </h1>');
    res.sendFile(path.join(__dirname , "public/index.html"));
});

app.listen (PORT, () => {
    console.log(`server is listening at http://localhost:${PORT}`);
});
