const express = require('express');
const path = require('path');
const { execFile } = require('child_process');
const bodyParser = require('body-parser');

const app = express();

// Middleware setup
app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: true }));

// Set EJS as view engine
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Serve the form page
app.get('/', (req, res) => {
  res.render('index'); // This will render views/index.ejs
});

// Handle form submission
app.post('/predict', (req, res) => {
  const age = req.body.age;
  const gender = req.body.gender;

  execFile('python', ['predict.py', age, gender], (error, stdout, stderr) => {
    if (error) {
      console.error('Error running Python script:', error);
      return res.send('An error occurred while predicting.');
    }

    const prediction = stdout.trim();
    res.render('result', { age, gender, prediction }); // This renders views/result.ejs
  });
});

// Start the server
app.listen(3000, () => {
  console.log('✅ Server is running at http://localhost:3000');
});
