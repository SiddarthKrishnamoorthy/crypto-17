var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { auth: false, get: true });
});

router.post('/', function(req, res, next) {
  if (req.body.name === req.cookies.userid) {
    var decoded = new Buffer(req.cookies.auth.toString(), 'base64').toString('utf-8');
    if (req.cookies.userid === decoded && req.cookies.userid === 'noone') {
      return res.render('index', { auth: true, get: false });
    }
  } else {
    res.cookie('userid', req.body.name);
    res.cookie('auth', new Buffer(req.body.name).toString('base64'));
  }
  res.render('index', { auth: false, get: false });
});

module.exports = router;
