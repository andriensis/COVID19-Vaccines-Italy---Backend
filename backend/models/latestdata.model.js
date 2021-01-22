const mongoose = require('mongoose');
const { toJSON } = require('./plugins');

const latestDataSchema = mongoose.Schema(
  {
    doses_administered: {
      type: Number
    },
    doses_delivered: {
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
