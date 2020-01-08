// ==UserScript==
// @name         New Userscript
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        *://*.youtube.com/*
// @grant        none
// ==/UserScript==

var input=document.createElement("input");
input.type="button";
input.value="GreaseMonkey Button";
input.onclick = showAlert;
input.style.z-index = '0'
document.body.appendChild(input);

function showAlert()
{
    alert("Hello World");
}


