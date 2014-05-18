var express = require('express'),
	ideb = require('./api/models/ideb.js');

var app = express();
 
app.configure(function () {
    app.use(express.logger('dev'));     /* 'default', 'short', 'tiny', 'dev' */
    app.use(express.bodyParser());
});

app.get('/v1/ideb/', ideb.findAllMunicipios);

app.get('/v1/ideb/:uf', ideb.findMunicipiosByUF);	
//app.get('/v1/ideb/:uf/:ano', ideb.filterByUFandAno);

//app.get('/v1/ideb/:uf/municipio/:codigo_municipio', ideb.findOneMunicipio);
app.post('/v1/ideb/:uf/municipio', ideb.addMunicipio);
//app.put('/v1/ideb/:uf/municipio/:codigo_municipio', ideb.updateMunicipio);
//app.delete('/v1/ideb/:uf/municipio/:codigo_municipio', ideb.deleteMunicipio);

app.listen(3000);
console.log('Listening on port 3000...');