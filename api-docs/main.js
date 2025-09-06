
const express = require('express');
const swaggerUi = require('swagger-ui-express');
const fs = require('fs');
const path = require('path');

const app = express();
const port = 3000;


const docsDir = __dirname;
const mergedSwaggerPath = path.join(docsDir, 'swagger.json');
if (fs.existsSync(mergedSwaggerPath)) {
	const swaggerDocument = require(mergedSwaggerPath);
	app.use('', swaggerUi.serve, swaggerUi.setup(swaggerDocument));
	console.log('Swagger UI available');
} else {
	console.error('swagger.json not found. Please run the merge script first.');
}

app.get('/', (req, res) => {
	res.send('API Docs available at /docs/<name>');
});

app.listen(port, () => {
	console.log(`API docs server running at http://localhost:${port}`);
});
