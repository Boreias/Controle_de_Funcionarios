const express = require('express');
const bodyParser = require('body-parser');

const app = express();

//Servidor
let porta = 8080;
app.listen(porta, () => {
 console.log('Servidor em execução na porta: ' + porta);
});

const Pessoa = require('./model/dbPessoa');


const MongoClient = require('mongodb').MongoClient;
const uri = 'mongodb+srv://Daniel95:Aguiar95@cluster0.zlppx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
const database_name = 'SRS';
const collection_name= 'Pessoa';
var db;
MongoClient.connect(uri, { useNewUrlParser: true, useUnifiedTopology: true }, (error, client) => {
        if(error) {
            console.log('ERRO: não foi possível conectar à base de dados ` ' + database_name + ' `.');
            throw error;
        }
        db = client.db(database_name).collection(collection_name);
        console.log('Conectado à base de dados ` ' + database_name + ' `!');
    });

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));

app.post('/Cadastro', (req, res, next) => {
    var cadastro = new Pessoa({
        "identificador": req.body.identificador,
        "nome": req.body.nome,
        "cpf": req.body.cpf,
        "idade": req.body.idade,
        "telefone": req.body.telefone
     });
    db.insertOne(cadastro, (err, result) => {
        if (err) return console.log("Error: " + err);
        console.log('Funcionario cadastrado com sucesso!');
        res.send('Funcionario cadastrado com sucesso!');
    });
});

app.get('/Cadastro', (req, res, next) => {
    db.find({}).toArray((err, result) => {
        if (err) return console.log("Error: " + err);
        res.send(result);
    });
});

app.get('/Cadastro/:identificador', (req, res, next) => {
    const result = db.findOne({ "identificador": req.params.identificador }, (err, result) => {
    if (err) return console.log("Funcionario não encontrado")
    res.send(result);
    });
});

app.put('/Cadastro/:identificador', (req, res, next) => {
    db.updateOne({"identificador": req.params.identificador }, {
        $set: {
          "nome": req.body.nome,
          "cpf": req.body.cpf,
          "idade": req.body.idade,
          "telefone": req.body.telefone
        }
    }, (err, result) => {
        if (err) return console.log("Error: " + err);
        console.log('Funcionario alterado com sucesso!');
        res.send('Funcionario alterado com sucesso!');
    });
});

app.delete('/Cadastro/:identificador', (req, res, next) => {
    db.deleteOne({"identificador": req.params.identificador },(err, result) => {
        if (err) return console.log("Error: " + err);
        console.log('Funcionario removido!');
        res.send('Funcionario removido!');
    });
});
