const thrift = require('thrift-http')
const TalkService = require('TalkService')
const {
  CancelChatInvitationRequest,
  DeleteOtherFromChatRequest
} = require('TalkService_types')

var line = '';
var gid = '';
var uids = [];
var method = '';
var token = '';
var appName = '';
var userAgent = '';

process.argv.forEach(function(val) {
  if (val.includes("gid=")) {
    gid = val.split("gid=").pop();
  } else if (val.includes("uid=")) {
    uids.push(val.split("uid=").pop());
  } else if (val.includes("method=")) {
    method = val.split("method=").pop();
  } else if (val.includes("token=")) {
    token = val.split("token=").pop();
  } else if (val.includes("appName=")) {
    appName = val.split("appName=").pop();
  } else if (val.includes("userAgent=")) {
    userAgent = val.split("userAgent=").pop();
  }
});

function setTHttpClient(options) {
  var connection = thrift.createHttpConnection("ga2.line.naver.jp", 443, options);
  connection.on("error", (err) => {
    console.log("err", err);
    return err;
  });
  line = thrift.createHttpClient(TalkService, connection);
}

setTHttpClient(options = {
  protocol: thrift.TCompactProtocol,
  transport: thrift.TBufferedTransport,
  headers: {
    "User-Agent": userAgent,
    "X-Line-Application": appName,
    "X-Line-Access": token
  },
  path: "/S4",
  https: true
});

if (method == 'cancel') {
  async function cancelAll() {
    let cancelPromise = new Promise((resolve, reject) => {
      try {
        for (var i = 0; i < uids.length; i++) {
          var request = new CancelChatInvitationRequest()
          request.reqSeq = 0;
          request.chatMid = gid;
          request.targetUserMids = [uids[i]]
          line.cancelChatInvitation(request);
        }
        resolve("CANCEL DONE")
      } catch (e) {
        reject(e);
      }
    });
    return cancelPromise;
  }
  var cancelPromise = cancelAll();
  Promise.all([cancelPromise])
  .then(results => console.log(results));
} else if (method == 'kick') {
  async function kickAll() {
    let kickPromise = new Promise((resolve, reject) => {
      try {
        for (var i = 0; i < uids.length; i++) {
          var request = new DeleteOtherFromChatRequest()
          request.reqSeq = 0;
          request.chatMid = gid;
          request.targetUserMids = [uids[i]]
          line.deleteOtherFromChat(request);
        }
        resolve("KICK DONE")
      } catch (e) {
        reject(e);
      }
    });
    return kickPromise;
  }
  var kickPromise = kickAll();
  Promise.all([kickPromise])
  .then(results => console.log(results));
}
