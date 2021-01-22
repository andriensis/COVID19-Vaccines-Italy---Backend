const mongoose = require('mongoose');
const { toJSON } = require('./plugins');

const administrationDataSchema = mongoose.Schema(
  {
    area: {
      type: String
    }
  }
);

administrationDataSchema.plugin(toJSON);

const AdministrationData = mongoose.model('administrationdata', administrationDataSchema, 'administrationdata');

module.exports = AdministrationData;
