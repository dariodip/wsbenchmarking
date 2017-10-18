const Sequelize = require('sequelize');


let personModel = {
    'id': {
        type: Sequelize.INTEGER,
        field: 'id',
        primaryKey: true
    },
    'name' : {
        type: Sequelize.STRING,
        field: 'name'
    },
    'surname' : {
        type: Sequelize.STRING,
        field: 'surname'
    },
    'city_id': {
        type: Sequelize.INTEGER,
        field: 'city_id'
    }
}

let cityModel = {
    'id' : {
        type: Sequelize.INTEGER,
        field: 'id',
        primaryKey: true
    },
    'name' : {
        type: Sequelize.STRING,
        field: 'name'
    },
    'post_code' : {
        type: Sequelize.STRING,
        field: 'post_code'
    },
    'region' : {
        type: Sequelize.STRING,
        field: 'region'
    }
}

module.exports.city = cityModel;
module.exports.person = personModel;