const express = require('express');
const router = express.Router();
const fib = require('../utils/fibonacci');
const person = require('../data/db').person;
const city = require('../data/db').city;

router.get('/hello_world', function (req, res, next) {
    res.send({'hello': 'World'});
});

router.get('/hello/:user', function (req, res, next) {
    res.send({'hello': req.params.user});
});

router.get('/fib30', function (req, res, next) {
    res.send({'fibonacci30': fib(30)});
});


router.get('/single_user', function (req, res, next) {
    let userInstance = person
        .findOne()
        .then(usr => {
            res.send({'user': usr.dataValues});
        })
        .catch(err => {
            res.send({'error': 'Error in fetching'});
        });
});

router.get('/all_users', function(req, res, next) {
    person.findAll()
    .then(users => {
        res.send({'users' : users.map(user => user.dataValues) });
    })
    .catch(err => {
        res.send({'error': 'Error in fetching'})
    });
});

router.get('/users_with_cities', function(req, res, next) {
    person.findAll({include: {model: city}})
    .then(users => {
        res.send({'users' : users.map(user => user.dataValues) });        
    })
    .catch(err => {
        res.send({'error': 'Error in fetching'})
    });
});

module.exports = router;
