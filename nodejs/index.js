// Developed by Dario Di Pasquale 

const express = require('express');
const app = express();
const PORT = 3000;
const fibonacci = require('./utils/fibonacci');
const db = require('./data/db');
const person = require('./data/db').person;
const city = require('./data/db').city;

app.get('/hello_world', (req, res) => {
    res.send({'hello' : 'World'});
});

app.get('/hello/:user', (req, res) => {
    res.send({'hello' : req.params.user});
});

app.get('/fib30', (req, res) => {
    res.send({'fibonacci30': fibonacci(30)});
});

app.get('/single_user', (req, res) => {
    let userInstance = person.findOne()
        .then(usr => {
            res.send({'user' : usr.dataValues});
        })
        .catch(err => {
            res.send({'error': 'Error in fetching'});
        });
});

app.get('/all_users', (req, res) => {
    person.findAll()
    .then(users => {
        res.send({'users' : users.map(user => user.dataValues) });
    })
    .catch(err => {
        res.send({'error': 'Error in fetching'})
    });
});

app.get('/users_with_cities', (req, res) => {
    person.findAll({include: {model: city}})
    .then(users => {
        res.send({'users' : users.map(user => user.dataValues) });        
    })
    .catch(err => {
        res.send({'error': 'Error in fetching'})
    });
});



app.listen(3000, () => {
    console.log(`Server running on ${PORT}`);
});