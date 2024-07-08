// server.js

const express = require('express');
const app = express();
const cors = require('cors');

app.use(cors()); // Allow all CORS requests (for testing purposes)

app.get('/greet', (req, res) => {
    res.json({ message: 'Hello from the Backend!' });
});

const port = 3000;
app.listen(port, () => {
    console.log(`Backend service running on port ${port}`);
});
