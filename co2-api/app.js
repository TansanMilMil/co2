const express = require('express')
const cors = require('cors')
const app = express()
const port = 3000
const mysql = require('mysql2')
const conn = mysql.createConnection({
	host: 'localhost',
	user: 'raspberrypi',
	password: 'raspberrypi',
	database: 'co2_observe'
});

conn.connect((err) => {
	if (err) {
		console.error(err.stack);
		return;
	}
	console.log('mysql connection success');
});

app.use(cors());

app.get('/LatestCo2', (req, res) => {
	conn.query(
		`
			SELECT *
			FROM co2
			ORDER BY created_at DESC
			LIMIT 1
		`
		, (err, result) => {
			res.send(result);
		}
	);
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
});

