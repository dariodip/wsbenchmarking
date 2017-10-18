const path = require('path');
const Sequelize = require('sequelize');

const basename = path.basename(module.filename);
const env = process.env.NODE_ENV || 'development';
const config = require(path.join(__dirname, '.', 'config.js'))[env];


const db = {};
const sequelize = new Sequelize(config.database, config.username, config.password, config);

sequelize
    .authenticate()
    .then(() => {
        console.log('Connection with database has been established successfully.');
    })
    .catch(err => {
        console.error('Unable to connect to the database:', err);
    });


const cityModel = require('./models').city;
const personModel = require('./models').person;

const City = sequelize.define('city', cityModel, 
                                {tableName: 'city',  
                                 timestamps: false});

const Person = sequelize.define('person', personModel, 
                                {tableName: 'person',  
                                 timestamps: false});

Person.belongsTo(City, {
    foreignKey: 'city_id',
    targetKey: 'id'
});

module.exports.seq = sequelize;
module.exports.city = City;
module.exports.person = Person;