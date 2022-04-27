const { Int32 } = require('mongodb');
const mongoose = require('mongoose');
const Schema = mongoose.Schema;
const PessoaSchema = new Schema({
   identificador: {
  type: String, 
  required: [true, 'Identificador Obrigatório'], 
  max: 100
  },
  nome: {
    type: String,
    required: [true, 'Nome é Obrigatório'],
    max: 150
  },
 cpf: {
  type: String, 
  required: [true, 'CPF é Obrigatória'], 
  max: 11
  },
  idade: {
      type: String,
      required: [true, 'Idade é Obrigatório'],
      max: 3
  },
  telefone: {
      type: String,
      required: [false],
      max: 9
  }
 });
 
module.exports = mongoose.model('Pessoa', PessoaSchema);