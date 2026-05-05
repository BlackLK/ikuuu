// ==UserScript==
// @name         ikuuu 自动签到
// @namespace    https://github.com/BlackLK/ikuuu
// @version      1.0.0
// @description  适用于脚本猫 / 篡改猴的 ikuuu.win 自动签到脚本，需要先在浏览器中完成登录和验证
// @author       BlackLK
// @match        https://ikuuu.win/*
// @grant        GM_notification
// @grant        GM_getValue
// @grant        GM_setValue
// @run-at       document-end
// ==/UserScript==

(function () {
  'use strict';

  const CHECKIN_URL = 'https://ikuuu.win/user/checkin';
  const LAST_CHECKIN_KEY = 'ikuuu_last_checkin_date';

  function today() {
    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0');
    const day = String(now.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
  }

  function notify(title, text) {
    if (typeof GM_notification === 'function') {
      GM_notification({ title, text, timeout: 5000 });
    } else if (typeof GM !== 'undefined' && typeof GM.notification === 'function') {
      GM.notification({ title, text, timeout: 5000 });
    } else {
      console.log(`${title}: ${text}`);
    }
  }

  function checkin() {
    fetch(CHECKIN_URL, {
      method: 'POST',
      credentials: 'include',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
      },
    })
      .then(function (response) {
        return response.text();
      })
      .then(function (responseText) {
        let message = responseText;
        try {
          const data = JSON.parse(responseText);
          message = data.msg || responseText;
        } catch (error) {
          message = '签到接口返回内容不是 JSON，可能未登录或页面发生变化';
        }

        GM_setValue(LAST_CHECKIN_KEY, today());
        notify('ikuuu 自动签到', message);
        console.log('[ikuuu 自动签到]', message);
      })
      .catch(function () {
        notify('ikuuu 自动签到', '请求签到接口失败');
      });
  }

  function main() {
    if (!location.href.startsWith('https://ikuuu.win/')) {
      return;
    }

    const lastCheckinDate = GM_getValue(LAST_CHECKIN_KEY, '');
    if (lastCheckinDate === today()) {
      console.log('[ikuuu 自动签到] 今日已执行过，跳过');
      return;
    }

    setTimeout(checkin, 3000);
  }

  main();
})();
