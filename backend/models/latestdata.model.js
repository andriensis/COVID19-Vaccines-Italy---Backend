const mongoose = require('mongoose');
const { toJSON } = require('./plugins');

const latestDataSchema = mongoose.Schema(
  {
    area: {
      type: String
    },
    doses_administered: {
      type: Number
    },
    doses_delivered: {
      type: Number
    },
    total_vaccinated: {
      type: Number
    },
    last_update: {
      type: Date
    }
  }
);

latestDataSchema.plugin(toJSON);

const LatestData = mongoose.model('latestdata', latestDataSchema, 'latestdata');

module.exports = LatestData;
