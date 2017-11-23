const express = require('express');
const router = express.Router();
const fib = require('../utils/fibonacci');
const person = require('../data/db').person;
const city = require('../data/db').city;

String.prototype.capitalize = function() {
    return this.charAt(0).toUpperCase() + this.slice(1);
};

router.get('/hello_world', function (req, res, next) {
    res.render('hello_world.ejs')
});

router.get('/hello/:user', function (req, res, next) {
    res.render('hello_user.ejs', {user: req.params.user.capitalize() });
});

router.get('/fib30', function (req, res, next) {
    const fibNum = fib(30);
    res.render('fib30.ejs', {fib: fibNum});
});


router.get('/single_user', function (req, res, next) {
    let userInstance = person
        .findOne()
        .then(usr => {
            res.render('single_user.ejs', {user: usr.dataValues});
        })
        .catch(err => {
            res.send({'error': 'Error in fetching'});
        });
});

router.get('/all_users', function(req, res, next) {
    person.findAll()
        .then(users => {
            res.render('all_users.ejs', {users: users.map(user => user.dataValues)});
        })
        .catch(err => {
            res.send({'error': 'Error in fetching'})
        });
});

router.get('/users_with_cities', function(req, res, next) {
    person.findAll({include: {model: city}})
        .then(users => {
            res.render('user_with_cities.ejs', {uwc: users.map(user => clearUsersWithCities(user))});
        })
        .catch(err => {
            res.send({'error': 'Error in fetching'})
        });
});

function clearUsersWithCities(uwc) {
    let userDataValues = uwc.dataValues;
    userDataValues.city = userDataValues.city.dataValues;
    return userDataValues;
}

module.exports = router;
