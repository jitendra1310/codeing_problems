/*
 * Author : Jitendra
 * Date: 12-Jun-2019
 * https://web-push-codelab.glitch.me/
 * Description : Push Notifications ,eslint-env browser, es6 
 * Public Key:BCso0UCoj4M5sKxRPx-NOlzXsPaqPrT-WgYuL6hZOn-nt-kZSvVgaxGXI7LXzdyG4BNvkXgGR1ErFYQILGLRv5o
 * Private Key:XWa53XK203Rk3p2NAsJ0Xrox8cSOqeUDcip5CZruibE
 */

'use strict';
const applicationServerPublicKey = 'BCso0UCoj4M5sKxRPx-NOlzXsPaqPrT-WgYuL6hZOn-nt-kZSvVgaxGXI7LXzdyG4BNvkXgGR1ErFYQILGLRv5o';
let isSubscribed = false;
let swRegistration = null;

if ('serviceWorker' in navigator && 'PushManager' in window) {
//  console.log('Service Worker and Push is supported');

  navigator.serviceWorker.register('sw.js')
  .then(function(swReg) {
    //console.log('Service Worker is registered', swReg);
    swRegistration = swReg;
    initializeUI();
  })
  .catch(function(error) {
    console.error('Service Worker Error', error);
  });
} else {
  console.warn('Push messaging is not supported');  
}


function initializeUI() {
  // Set the initial subscription value
  swRegistration.pushManager.getSubscription()
  .then(function(subscription) {
    isSubscribed = !(subscription === null);    
      subscribeUser();
    if (Notification.permission === 'denied') {          
        return;
    }

  });
}


function updateSubscriptionOnServer(subscription) {
  // TODO: Send subscription to application server
  const subscriptionJson = document.querySelector('.js-subscription-json');
  if (subscription) {
    var postData = JSON.stringify(subscription);
    console.log(postData);
  }
}

function subscribeUser() {
  const applicationServerKey = urlB64ToUint8Array(applicationServerPublicKey);
  swRegistration.pushManager.subscribe({
    userVisibleOnly: true,
    applicationServerKey: applicationServerKey
  })
  .then(function(subscription) {
    //console.log('User is subscribed.');
    if(Notification.permission=='granted'){
      var postData = JSON.stringify(subscription);     
      console.log(postData);
    }
  });

}


function urlB64ToUint8Array(base64String) {
  const padding = '='.repeat((4 - base64String.length % 4) % 4);
  const base64 = (base64String + padding)
    .replace(/\-/g, '+')
    .replace(/_/g, '/');

  const rawData = window.atob(base64);
  const outputArray = new Uint8Array(rawData.length);

  for (let i = 0; i < rawData.length; ++i) {
    outputArray[i] = rawData.charCodeAt(i);
  }
  return outputArray;
}
