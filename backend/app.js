const express = require('express')
const app = express()
require('dotenv').config();
const port = process.env.PORT || 3000
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const LatestData = require('./models/latestdata.model');
const AdministrationData = require('./models/administrationdata.model');

mongoose.connect(process.env.MONGODB_URL, {
  useCreateIndex: true,
  useNewUrlParser: true,
  useUnifiedTopology: true,
}).then(() => {
  console.log('Connected to MongoDB');
});

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.get('/latestData', async (req, res) => {
  const latestData = await LatestData.find()
  var summaryData = {
    'doses_administered': 0,
    'doses_delivered': 0,
    'administration_percentage': 0,
    'last_update': ''
  }
  var lastUpdate
  for (const regionData of latestData) {
    summaryData.doses_delivered += regionData.doses_delivered
    summaryData.doses_administered += regionData.doses_administered
    if (!lastUpdate || regionData.lastUpdate > lastUpdate) {
      lastUpdate = regionData.last_update
    }
  }
  summaryData.administration_percentage = Number((summaryData.doses_administered / summaryData.doses_delivered * 100).toFixed(1))
  summaryData.last_update = lastUpdate

  res.send({ "summary": summaryData, "details": latestData })
})

app.get('/administrationData/:area', async (req, res) => {
  const administrationData = await AdministrationData.find({area: req.params.area})
  res.send(administrationData)
})

app.listen(port, () => {
  console.log('API server started on ' + port)
})
