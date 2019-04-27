<!DOCTYPE html>
<html>
<head><meta charset="utf-8" />

<title>notebook</title>

<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>



<style type="text/css">
    /*!
*
* Twitter Bootstrap
*
*/
/*!
 * Bootstrap v3.3.7 (http://getbootstrap.com)
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */
/*! normalize.css v3.0.3 | MIT License | github.com/necolas/normalize.css */
html {
  font-family: sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
}
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
menu,
nav,
section,
summary {
  display: block;
}
audio,
canvas,
progress,
video {
  display: inline-block;
  vertical-align: baseline;
}
audio:not([controls]) {
  display: none;
  height: 0;
}
[hidden],
template {
  display: none;
}
a {
  background-color: transparent;
}
a:active,
a:hover {
  outline: 0;
}
abbr[title] {
  border-bottom: 1px dotted;
}
b,
strong {
  font-weight: bold;
}
dfn {
  font-style: italic;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
mark {
  background: #ff0;
  color: #000;
}
small {
  font-size: 80%;
}
sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sup {
  top: -0.5em;
}
sub {
  bottom: -0.25em;
}
img {
  border: 0;
}
svg:not(:root) {
  overflow: hidden;
}
figure {
  margin: 1em 40px;
}
hr {
  box-sizing: content-box;
  height: 0;
}
pre {
  overflow: auto;
}
code,
kbd,
pre,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}
button,
input,
optgroup,
select,
textarea {
  color: inherit;
  font: inherit;
  margin: 0;
}
button {
  overflow: visible;
}
button,
select {
  text-transform: none;
}
button,
html input[type="button"],
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button;
  cursor: pointer;
}
button[disabled],
html input[disabled] {
  cursor: default;
}
button::-moz-focus-inner,
input::-moz-focus-inner {
  border: 0;
  padding: 0;
}
input {
  line-height: normal;
}
input[type="checkbox"],
input[type="radio"] {
  box-sizing: border-box;
  padding: 0;
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: textfield;
  box-sizing: content-box;
}
input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}
fieldset {
  border: 1px solid #c0c0c0;
  margin: 0 2px;
  padding: 0.35em 0.625em 0.75em;
}
legend {
  border: 0;
  padding: 0;
}
textarea {
  overflow: auto;
}
optgroup {
  font-weight: bold;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
td,
th {
  padding: 0;
}
/*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */
@media print {
  *,
  *:before,
  *:after {
    background: transparent !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }
  a,
  a:visited {
    text-decoration: underline;
  }
  a[href]:after {
    content: " (" attr(href) ")";
  }
  abbr[title]:after {
    content: " (" attr(title) ")";
  }
  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }
  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }
  thead {
    display: table-header-group;
  }
  tr,
  img {
    page-break-inside: avoid;
  }
  img {
    max-width: 100% !important;
  }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }
  h2,
  h3 {
    page-break-after: avoid;
  }
  .navbar {
    display: none;
  }
  .btn > .caret,
  .dropup > .btn > .caret {
    border-top-color: #000 !important;
  }
  .label {
    border: 1px solid #000;
  }
  .table {
    border-collapse: collapse !important;
  }
  .table td,
  .table th {
    background-color: #fff !important;
  }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #ddd !important;
  }
}
@font-face {
  font-family: 'Glyphicons Halflings';
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot');
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot?#iefix') format('embedded-opentype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff2') format('woff2'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff') format('woff'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.ttf') format('truetype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular') format('svg');
}
.glyphicon {
  position: relative;
  top: 1px;
  display: inline-block;
  font-family: 'Glyphicons Halflings';
  font-style: normal;
  font-weight: normal;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.glyphicon-asterisk:before {
  content: "\002a";
}
.glyphicon-plus:before {
  content: "\002b";
}
.glyphicon-euro:before,
.glyphicon-eur:before {
  content: "\20ac";
}
.glyphicon-minus:before {
  content: "\2212";
}
.glyphicon-cloud:before {
  content: "\2601";
}
.glyphicon-envelope:before {
  content: "\2709";
}
.glyphicon-pencil:before {
  content: "\270f";
}
.glyphicon-glass:before {
  content: "\e001";
}
.glyphicon-music:before {
  content: "\e002";
}
.glyphicon-search:before {
  content: "\e003";
}
.glyphicon-heart:before {
  content: "\e005";
}
.glyphicon-star:before {
  content: "\e006";
}
.glyphicon-star-empty:before {
  content: "\e007";
}
.glyphicon-user:before {
  content: "\e008";
}
.glyphicon-film:before {
  content: "\e009";
}
.glyphicon-th-large:before {
  content: "\e010";
}
.glyphicon-th:before {
  content: "\e011";
}
.glyphicon-th-list:before {
  content: "\e012";
}
.glyphicon-ok:before {
  content: "\e013";
}
.glyphicon-remove:before {
  content: "\e014";
}
.glyphicon-zoom-in:before {
  content: "\e015";
}
.glyphicon-zoom-out:before {
  content: "\e016";
}
.glyphicon-off:before {
  content: "\e017";
}
.glyphicon-signal:before {
  content: "\e018";
}
.glyphicon-cog:before {
  content: "\e019";
}
.glyphicon-trash:before {
  content: "\e020";
}
.glyphicon-home:before {
  content: "\e021";
}
.glyphicon-file:before {
  content: "\e022";
}
.glyphicon-time:before {
  content: "\e023";
}
.glyphicon-road:before {
  content: "\e024";
}
.glyphicon-download-alt:before {
  content: "\e025";
}
.glyphicon-download:before {
  content: "\e026";
}
.glyphicon-upload:before {
  content: "\e027";
}
.glyphicon-inbox:before {
  content: "\e028";
}
.glyphicon-play-circle:before {
  content: "\e029";
}
.glyphicon-repeat:before {
  content: "\e030";
}
.glyphicon-refresh:before {
  content: "\e031";
}
.glyphicon-list-alt:before {
  content: "\e032";
}
.glyphicon-lock:before {
  content: "\e033";
}
.glyphicon-flag:before {
  content: "\e034";
}
.glyphicon-headphones:before {
  content: "\e035";
}
.glyphicon-volume-off:before {
  content: "\e036";
}
.glyphicon-volume-down:before {
  content: "\e037";
}
.glyphicon-volume-up:before {
  content: "\e038";
}
.glyphicon-qrcode:before {
  content: "\e039";
}
.glyphicon-barcode:before {
  content: "\e040";
}
.glyphicon-tag:before {
  content: "\e041";
}
.glyphicon-tags:before {
  content: "\e042";
}
.glyphicon-book:before {
  content: "\e043";
}
.glyphicon-bookmark:before {
  content: "\e044";
}
.glyphicon-print:before {
  content: "\e045";
}
.glyphicon-camera:before {
  content: "\e046";
}
.glyphicon-font:before {
  content: "\e047";
}
.glyphicon-bold:before {
  content: "\e048";
}
.glyphicon-italic:before {
  content: "\e049";
}
.glyphicon-text-height:before {
  content: "\e050";
}
.glyphicon-text-width:before {
  content: "\e051";
}
.glyphicon-align-left:before {
  content: "\e052";
}
.glyphicon-align-center:before {
  content: "\e053";
}
.glyphicon-align-right:before {
  content: "\e054";
}
.glyphicon-align-justify:before {
  content: "\e055";
}
.glyphicon-list:before {
  content: "\e056";
}
.glyphicon-indent-left:before {
  content: "\e057";
}
.glyphicon-indent-right:before {
  content: "\e058";
}
.glyphicon-facetime-video:before {
  content: "\e059";
}
.glyphicon-picture:before {
  content: "\e060";
}
.glyphicon-map-marker:before {
  content: "\e062";
}
.glyphicon-adjust:before {
  content: "\e063";
}
.glyphicon-tint:before {
  content: "\e064";
}
.glyphicon-edit:before {
  content: "\e065";
}
.glyphicon-share:before {
  content: "\e066";
}
.glyphicon-check:before {
  content: "\e067";
}
.glyphicon-move:before {
  content: "\e068";
}
.glyphicon-step-backward:before {
  content: "\e069";
}
.glyphicon-fast-backward:before {
  content: "\e070";
}
.glyphicon-backward:before {
  content: "\e071";
}
.glyphicon-play:before {
  content: "\e072";
}
.glyphicon-pause:before {
  content: "\e073";
}
.glyphicon-stop:before {
  content: "\e074";
}
.glyphicon-forward:before {
  content: "\e075";
}
.glyphicon-fast-forward:before {
  content: "\e076";
}
.glyphicon-step-forward:before {
  content: "\e077";
}
.glyphicon-eject:before {
  content: "\e078";
}
.glyphicon-chevron-left:before {
  content: "\e079";
}
.glyphicon-chevron-right:before {
  content: "\e080";
}
.glyphicon-plus-sign:before {
  content: "\e081";
}
.glyphicon-minus-sign:before {
  content: "\e082";
}
.glyphicon-remove-sign:before {
  content: "\e083";
}
.glyphicon-ok-sign:before {
  content: "\e084";
}
.glyphicon-question-sign:before {
  content: "\e085";
}
.glyphicon-info-sign:before {
  content: "\e086";
}
.glyphicon-screenshot:before {
  content: "\e087";
}
.glyphicon-remove-circle:before {
  content: "\e088";
}
.glyphicon-ok-circle:before {
  content: "\e089";
}
.glyphicon-ban-circle:before {
  content: "\e090";
}
.glyphicon-arrow-left:before {
  content: "\e091";
}
.glyphicon-arrow-right:before {
  content: "\e092";
}
.glyphicon-arrow-up:before {
  content: "\e093";
}
.glyphicon-arrow-down:before {
  content: "\e094";
}
.glyphicon-share-alt:before {
  content: "\e095";
}
.glyphicon-resize-full:before {
  content: "\e096";
}
.glyphicon-resize-small:before {
  content: "\e097";
}
.glyphicon-exclamation-sign:before {
  content: "\e101";
}
.glyphicon-gift:before {
  content: "\e102";
}
.glyphicon-leaf:before {
  content: "\e103";
}
.glyphicon-fire:before {
  content: "\e104";
}
.glyphicon-eye-open:before {
  content: "\e105";
}
.glyphicon-eye-close:before {
  content: "\e106";
}
.glyphicon-warning-sign:before {
  content: "\e107";
}
.glyphicon-plane:before {
  content: "\e108";
}
.glyphicon-calendar:before {
  content: "\e109";
}
.glyphicon-random:before {
  content: "\e110";
}
.glyphicon-comment:before {
  content: "\e111";
}
.glyphicon-magnet:before {
  content: "\e112";
}
.glyphicon-chevron-up:before {
  content: "\e113";
}
.glyphicon-chevron-down:before {
  content: "\e114";
}
.glyphicon-retweet:before {
  content: "\e115";
}
.glyphicon-shopping-cart:before {
  content: "\e116";
}
.glyphicon-folder-close:before {
  content: "\e117";
}
.glyphicon-folder-open:before {
  content: "\e118";
}
.glyphicon-resize-vertical:before {
  content: "\e119";
}
.glyphicon-resize-horizontal:before {
  content: "\e120";
}
.glyphicon-hdd:before {
  content: "\e121";
}
.glyphicon-bullhorn:before {
  content: "\e122";
}
.glyphicon-bell:before {
  content: "\e123";
}
.glyphicon-certificate:before {
  content: "\e124";
}
.glyphicon-thumbs-up:before {
  content: "\e125";
}
.glyphicon-thumbs-down:before {
  content: "\e126";
}
.glyphicon-hand-right:before {
  content: "\e127";
}
.glyphicon-hand-left:before {
  content: "\e128";
}
.glyphicon-hand-up:before {
  content: "\e129";
}
.glyphicon-hand-down:before {
  content: "\e130";
}
.glyphicon-circle-arrow-right:before {
  content: "\e131";
}
.glyphicon-circle-arrow-left:before {
  content: "\e132";
}
.glyphicon-circle-arrow-up:before {
  content: "\e133";
}
.glyphicon-circle-arrow-down:before {
  content: "\e134";
}
.glyphicon-globe:before {
  content: "\e135";
}
.glyphicon-wrench:before {
  content: "\e136";
}
.glyphicon-tasks:before {
  content: "\e137";
}
.glyphicon-filter:before {
  content: "\e138";
}
.glyphicon-briefcase:before {
  content: "\e139";
}
.glyphicon-fullscreen:before {
  content: "\e140";
}
.glyphicon-dashboard:before {
  content: "\e141";
}
.glyphicon-paperclip:before {
  content: "\e142";
}
.glyphicon-heart-empty:before {
  content: "\e143";
}
.glyphicon-link:before {
  content: "\e144";
}
.glyphicon-phone:before {
  content: "\e145";
}
.glyphicon-pushpin:before {
  content: "\e146";
}
.glyphicon-usd:before {
  content: "\e148";
}
.glyphicon-gbp:before {
  content: "\e149";
}
.glyphicon-sort:before {
  content: "\e150";
}
.glyphicon-sort-by-alphabet:before {
  content: "\e151";
}
.glyphicon-sort-by-alphabet-alt:before {
  content: "\e152";
}
.glyphicon-sort-by-order:before {
  content: "\e153";
}
.glyphicon-sort-by-order-alt:before {
  content: "\e154";
}
.glyphicon-sort-by-attributes:before {
  content: "\e155";
}
.glyphicon-sort-by-attributes-alt:before {
  content: "\e156";
}
.glyphicon-unchecked:before {
  content: "\e157";
}
.glyphicon-expand:before {
  content: "\e158";
}
.glyphicon-collapse-down:before {
  content: "\e159";
}
.glyphicon-collapse-up:before {
  content: "\e160";
}
.glyphicon-log-in:before {
  content: "\e161";
}
.glyphicon-flash:before {
  content: "\e162";
}
.glyphicon-log-out:before {
  content: "\e163";
}
.glyphicon-new-window:before {
  content: "\e164";
}
.glyphicon-record:before {
  content: "\e165";
}
.glyphicon-save:before {
  content: "\e166";
}
.glyphicon-open:before {
  content: "\e167";
}
.glyphicon-saved:before {
  content: "\e168";
}
.glyphicon-import:before {
  content: "\e169";
}
.glyphicon-export:before {
  content: "\e170";
}
.glyphicon-send:before {
  content: "\e171";
}
.glyphicon-floppy-disk:before {
  content: "\e172";
}
.glyphicon-floppy-saved:before {
  content: "\e173";
}
.glyphicon-floppy-remove:before {
  content: "\e174";
}
.glyphicon-floppy-save:before {
  content: "\e175";
}
.glyphicon-floppy-open:before {
  content: "\e176";
}
.glyphicon-credit-card:before {
  content: "\e177";
}
.glyphicon-transfer:before {
  content: "\e178";
}
.glyphicon-cutlery:before {
  content: "\e179";
}
.glyphicon-header:before {
  content: "\e180";
}
.glyphicon-compressed:before {
  content: "\e181";
}
.glyphicon-earphone:before {
  content: "\e182";
}
.glyphicon-phone-alt:before {
  content: "\e183";
}
.glyphicon-tower:before {
  content: "\e184";
}
.glyphicon-stats:before {
  content: "\e185";
}
.glyphicon-sd-video:before {
  content: "\e186";
}
.glyphicon-hd-video:before {
  content: "\e187";
}
.glyphicon-subtitles:before {
  content: "\e188";
}
.glyphicon-sound-stereo:before {
  content: "\e189";
}
.glyphicon-sound-dolby:before {
  content: "\e190";
}
.glyphicon-sound-5-1:before {
  content: "\e191";
}
.glyphicon-sound-6-1:before {
  content: "\e192";
}
.glyphicon-sound-7-1:before {
  content: "\e193";
}
.glyphicon-copyright-mark:before {
  content: "\e194";
}
.glyphicon-registration-mark:before {
  content: "\e195";
}
.glyphicon-cloud-download:before {
  content: "\e197";
}
.glyphicon-cloud-upload:before {
  content: "\e198";
}
.glyphicon-tree-conifer:before {
  content: "\e199";
}
.glyphicon-tree-deciduous:before {
  content: "\e200";
}
.glyphicon-cd:before {
  content: "\e201";
}
.glyphicon-save-file:before {
  content: "\e202";
}
.glyphicon-open-file:before {
  content: "\e203";
}
.glyphicon-level-up:before {
  content: "\e204";
}
.glyphicon-copy:before {
  content: "\e205";
}
.glyphicon-paste:before {
  content: "\e206";
}
.glyphicon-alert:before {
  content: "\e209";
}
.glyphicon-equalizer:before {
  content: "\e210";
}
.glyphicon-king:before {
  content: "\e211";
}
.glyphicon-queen:before {
  content: "\e212";
}
.glyphicon-pawn:before {
  content: "\e213";
}
.glyphicon-bishop:before {
  content: "\e214";
}
.glyphicon-knight:before {
  content: "\e215";
}
.glyphicon-baby-formula:before {
  content: "\e216";
}
.glyphicon-tent:before {
  content: "\26fa";
}
.glyphicon-blackboard:before {
  content: "\e218";
}
.glyphicon-bed:before {
  content: "\e219";
}
.glyphicon-apple:before {
  content: "\f8ff";
}
.glyphicon-erase:before {
  content: "\e221";
}
.glyphicon-hourglass:before {
  content: "\231b";
}
.glyphicon-lamp:before {
  content: "\e223";
}
.glyphicon-duplicate:before {
  content: "\e224";
}
.glyphicon-piggy-bank:before {
  content: "\e225";
}
.glyphicon-scissors:before {
  content: "\e226";
}
.glyphicon-bitcoin:before {
  content: "\e227";
}
.glyphicon-btc:before {
  content: "\e227";
}
.glyphicon-xbt:before {
  content: "\e227";
}
.glyphicon-yen:before {
  content: "\00a5";
}
.glyphicon-jpy:before {
  content: "\00a5";
}
.glyphicon-ruble:before {
  content: "\20bd";
}
.glyphicon-rub:before {
  content: "\20bd";
}
.glyphicon-scale:before {
  content: "\e230";
}
.glyphicon-ice-lolly:before {
  content: "\e231";
}
.glyphicon-ice-lolly-tasted:before {
  content: "\e232";
}
.glyphicon-education:before {
  content: "\e233";
}
.glyphicon-option-horizontal:before {
  content: "\e234";
}
.glyphicon-option-vertical:before {
  content: "\e235";
}
.glyphicon-menu-hamburger:before {
  content: "\e236";
}
.glyphicon-modal-window:before {
  content: "\e237";
}
.glyphicon-oil:before {
  content: "\e238";
}
.glyphicon-grain:before {
  content: "\e239";
}
.glyphicon-sunglasses:before {
  content: "\e240";
}
.glyphicon-text-size:before {
  content: "\e241";
}
.glyphicon-text-color:before {
  content: "\e242";
}
.glyphicon-text-background:before {
  content: "\e243";
}
.glyphicon-object-align-top:before {
  content: "\e244";
}
.glyphicon-object-align-bottom:before {
  content: "\e245";
}
.glyphicon-object-align-horizontal:before {
  content: "\e246";
}
.glyphicon-object-align-left:before {
  content: "\e247";
}
.glyphicon-object-align-vertical:before {
  content: "\e248";
}
.glyphicon-object-align-right:before {
  content: "\e249";
}
.glyphicon-triangle-right:before {
  content: "\e250";
}
.glyphicon-triangle-left:before {
  content: "\e251";
}
.glyphicon-triangle-bottom:before {
  content: "\e252";
}
.glyphicon-triangle-top:before {
  content: "\e253";
}
.glyphicon-console:before {
  content: "\e254";
}
.glyphicon-superscript:before {
  content: "\e255";
}
.glyphicon-subscript:before {
  content: "\e256";
}
.glyphicon-menu-left:before {
  content: "\e257";
}
.glyphicon-menu-right:before {
  content: "\e258";
}
.glyphicon-menu-down:before {
  content: "\e259";
}
.glyphicon-menu-up:before {
  content: "\e260";
}
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
*:before,
*:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
html {
  font-size: 10px;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  line-height: 1.42857143;
  color: #000;
  background-color: #fff;
}
input,
button,
select,
textarea {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}
a {
  color: #337ab7;
  text-decoration: none;
}
a:hover,
a:focus {
  color: #23527c;
  text-decoration: underline;
}
a:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
figure {
  margin: 0;
}
img {
  vertical-align: middle;
}
.img-responsive,
.thumbnail > img,
.thumbnail a > img,
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  display: block;
  max-width: 100%;
  height: auto;
}
.img-rounded {
  border-radius: 3px;
}
.img-thumbnail {
  padding: 4px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
  display: inline-block;
  max-width: 100%;
  height: auto;
}
.img-circle {
  border-radius: 50%;
}
hr {
  margin-top: 18px;
  margin-bottom: 18px;
  border: 0;
  border-top: 1px solid #eeeeee;
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
[role="button"] {
  cursor: pointer;
}
h1,
h2,
h3,
h4,
h5,
h6,
.h1,
.h2,
.h3,
.h4,
.h5,
.h6 {
  font-family: inherit;
  font-weight: 500;
  line-height: 1.1;
  color: inherit;
}
h1 small,
h2 small,
h3 small,
h4 small,
h5 small,
h6 small,
.h1 small,
.h2 small,
.h3 small,
.h4 small,
.h5 small,
.h6 small,
h1 .small,
h2 .small,
h3 .small,
h4 .small,
h5 .small,
h6 .small,
.h1 .small,
.h2 .small,
.h3 .small,
.h4 .small,
.h5 .small,
.h6 .small {
  font-weight: normal;
  line-height: 1;
  color: #777777;
}
h1,
.h1,
h2,
.h2,
h3,
.h3 {
  margin-top: 18px;
  margin-bottom: 9px;
}
h1 small,
.h1 small,
h2 small,
.h2 small,
h3 small,
.h3 small,
h1 .small,
.h1 .small,
h2 .small,
.h2 .small,
h3 .small,
.h3 .small {
  font-size: 65%;
}
h4,
.h4,
h5,
.h5,
h6,
.h6 {
  margin-top: 9px;
  margin-bottom: 9px;
}
h4 small,
.h4 small,
h5 small,
.h5 small,
h6 small,
.h6 small,
h4 .small,
.h4 .small,
h5 .small,
.h5 .small,
h6 .small,
.h6 .small {
  font-size: 75%;
}
h1,
.h1 {
  font-size: 33px;
}
h2,
.h2 {
  font-size: 27px;
}
h3,
.h3 {
  font-size: 23px;
}
h4,
.h4 {
  font-size: 17px;
}
h5,
.h5 {
  font-size: 13px;
}
h6,
.h6 {
  font-size: 12px;
}
p {
  margin: 0 0 9px;
}
.lead {
  margin-bottom: 18px;
  font-size: 14px;
  font-weight: 300;
  line-height: 1.4;
}
@media (min-width: 768px) {
  .lead {
    font-size: 19.5px;
  }
}
small,
.small {
  font-size: 92%;
}
mark,
.mark {
  background-color: #fcf8e3;
  padding: .2em;
}
.text-left {
  text-align: left;
}
.text-right {
  text-align: right;
}
.text-center {
  text-align: center;
}
.text-justify {
  text-align: justify;
}
.text-nowrap {
  white-space: nowrap;
}
.text-lowercase {
  text-transform: lowercase;
}
.text-uppercase {
  text-transform: uppercase;
}
.text-capitalize {
  text-transform: capitalize;
}
.text-muted {
  color: #777777;
}
.text-primary {
  color: #337ab7;
}
a.text-primary:hover,
a.text-primary:focus {
  color: #286090;
}
.text-success {
  color: #3c763d;
}
a.text-success:hover,
a.text-success:focus {
  color: #2b542c;
}
.text-info {
  color: #31708f;
}
a.text-info:hover,
a.text-info:focus {
  color: #245269;
}
.text-warning {
  color: #8a6d3b;
}
a.text-warning:hover,
a.text-warning:focus {
  color: #66512c;
}
.text-danger {
  color: #a94442;
}
a.text-danger:hover,
a.text-danger:focus {
  color: #843534;
}
.bg-primary {
  color: #fff;
  background-color: #337ab7;
}
a.bg-primary:hover,
a.bg-primary:focus {
  background-color: #286090;
}
.bg-success {
  background-color: #dff0d8;
}
a.bg-success:hover,
a.bg-success:focus {
  background-color: #c1e2b3;
}
.bg-info {
  background-color: #d9edf7;
}
a.bg-info:hover,
a.bg-info:focus {
  background-color: #afd9ee;
}
.bg-warning {
  background-color: #fcf8e3;
}
a.bg-warning:hover,
a.bg-warning:focus {
  background-color: #f7ecb5;
}
.bg-danger {
  background-color: #f2dede;
}
a.bg-danger:hover,
a.bg-danger:focus {
  background-color: #e4b9b9;
}
.page-header {
  padding-bottom: 8px;
  margin: 36px 0 18px;
  border-bottom: 1px solid #eeeeee;
}
ul,
ol {
  margin-top: 0;
  margin-bottom: 9px;
}
ul ul,
ol ul,
ul ol,
ol ol {
  margin-bottom: 0;
}
.list-unstyled {
  padding-left: 0;
  list-style: none;
}
.list-inline {
  padding-left: 0;
  list-style: none;
  margin-left: -5px;
}
.list-inline > li {
  display: inline-block;
  padding-left: 5px;
  padding-right: 5px;
}
dl {
  margin-top: 0;
  margin-bottom: 18px;
}
dt,
dd {
  line-height: 1.42857143;
}
dt {
  font-weight: bold;
}
dd {
  margin-left: 0;
}
@media (min-width: 541px) {
  .dl-horizontal dt {
    float: left;
    width: 160px;
    clear: left;
    text-align: right;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .dl-horizontal dd {
    margin-left: 180px;
  }
}
abbr[title],
abbr[data-original-title] {
  cursor: help;
  border-bottom: 1px dotted #777777;
}
.initialism {
  font-size: 90%;
  text-transform: uppercase;
}
blockquote {
  padding: 9px 18px;
  margin: 0 0 18px;
  font-size: inherit;
  border-left: 5px solid #eeeeee;
}
blockquote p:last-child,
blockquote ul:last-child,
blockquote ol:last-child {
  margin-bottom: 0;
}
blockquote footer,
blockquote small,
blockquote .small {
  display: block;
  font-size: 80%;
  line-height: 1.42857143;
  color: #777777;
}
blockquote footer:before,
blockquote small:before,
blockquote .small:before {
  content: '\2014 \00A0';
}
.blockquote-reverse,
blockquote.pull-right {
  padding-right: 15px;
  padding-left: 0;
  border-right: 5px solid #eeeeee;
  border-left: 0;
  text-align: right;
}
.blockquote-reverse footer:before,
blockquote.pull-right footer:before,
.blockquote-reverse small:before,
blockquote.pull-right small:before,
.blockquote-reverse .small:before,
blockquote.pull-right .small:before {
  content: '';
}
.blockquote-reverse footer:after,
blockquote.pull-right footer:after,
.blockquote-reverse small:after,
blockquote.pull-right small:after,
.blockquote-reverse .small:after,
blockquote.pull-right .small:after {
  content: '\00A0 \2014';
}
address {
  margin-bottom: 18px;
  font-style: normal;
  line-height: 1.42857143;
}
code,
kbd,
pre,
samp {
  font-family: monospace;
}
code {
  padding: 2px 4px;
  font-size: 90%;
  color: #c7254e;
  background-color: #f9f2f4;
  border-radius: 2px;
}
kbd {
  padding: 2px 4px;
  font-size: 90%;
  color: #888;
  background-color: transparent;
  border-radius: 1px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
}
kbd kbd {
  padding: 0;
  font-size: 100%;
  font-weight: bold;
  box-shadow: none;
}
pre {
  display: block;
  padding: 8.5px;
  margin: 0 0 9px;
  font-size: 12px;
  line-height: 1.42857143;
  word-break: break-all;
  word-wrap: break-word;
  color: #333333;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 2px;
}
pre code {
  padding: 0;
  font-size: inherit;
  color: inherit;
  white-space: pre-wrap;
  background-color: transparent;
  border-radius: 0;
}
.pre-scrollable {
  max-height: 340px;
  overflow-y: scroll;
}
.container {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
@media (min-width: 768px) {
  .container {
    width: 768px;
  }
}
@media (min-width: 992px) {
  .container {
    width: 940px;
  }
}
@media (min-width: 1200px) {
  .container {
    width: 1140px;
  }
}
.container-fluid {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
.row {
  margin-left: 0px;
  margin-right: 0px;
}
.col-xs-1, .col-sm-1, .col-md-1, .col-lg-1, .col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3, .col-xs-4, .col-sm-4, .col-md-4, .col-lg-4, .col-xs-5, .col-sm-5, .col-md-5, .col-lg-5, .col-xs-6, .col-sm-6, .col-md-6, .col-lg-6, .col-xs-7, .col-sm-7, .col-md-7, .col-lg-7, .col-xs-8, .col-sm-8, .col-md-8, .col-lg-8, .col-xs-9, .col-sm-9, .col-md-9, .col-lg-9, .col-xs-10, .col-sm-10, .col-md-10, .col-lg-10, .col-xs-11, .col-sm-11, .col-md-11, .col-lg-11, .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-left: 0px;
  padding-right: 0px;
}
.col-xs-1, .col-xs-2, .col-xs-3, .col-xs-4, .col-xs-5, .col-xs-6, .col-xs-7, .col-xs-8, .col-xs-9, .col-xs-10, .col-xs-11, .col-xs-12 {
  float: left;
}
.col-xs-12 {
  width: 100%;
}
.col-xs-11 {
  width: 91.66666667%;
}
.col-xs-10 {
  width: 83.33333333%;
}
.col-xs-9 {
  width: 75%;
}
.col-xs-8 {
  width: 66.66666667%;
}
.col-xs-7 {
  width: 58.33333333%;
}
.col-xs-6 {
  width: 50%;
}
.col-xs-5 {
  width: 41.66666667%;
}
.col-xs-4 {
  width: 33.33333333%;
}
.col-xs-3 {
  width: 25%;
}
.col-xs-2 {
  width: 16.66666667%;
}
.col-xs-1 {
  width: 8.33333333%;
}
.col-xs-pull-12 {
  right: 100%;
}
.col-xs-pull-11 {
  right: 91.66666667%;
}
.col-xs-pull-10 {
  right: 83.33333333%;
}
.col-xs-pull-9 {
  right: 75%;
}
.col-xs-pull-8 {
  right: 66.66666667%;
}
.col-xs-pull-7 {
  right: 58.33333333%;
}
.col-xs-pull-6 {
  right: 50%;
}
.col-xs-pull-5 {
  right: 41.66666667%;
}
.col-xs-pull-4 {
  right: 33.33333333%;
}
.col-xs-pull-3 {
  right: 25%;
}
.col-xs-pull-2 {
  right: 16.66666667%;
}
.col-xs-pull-1 {
  right: 8.33333333%;
}
.col-xs-pull-0 {
  right: auto;
}
.col-xs-push-12 {
  left: 100%;
}
.col-xs-push-11 {
  left: 91.66666667%;
}
.col-xs-push-10 {
  left: 83.33333333%;
}
.col-xs-push-9 {
  left: 75%;
}
.col-xs-push-8 {
  left: 66.66666667%;
}
.col-xs-push-7 {
  left: 58.33333333%;
}
.col-xs-push-6 {
  left: 50%;
}
.col-xs-push-5 {
  left: 41.66666667%;
}
.col-xs-push-4 {
  left: 33.33333333%;
}
.col-xs-push-3 {
  left: 25%;
}
.col-xs-push-2 {
  left: 16.66666667%;
}
.col-xs-push-1 {
  left: 8.33333333%;
}
.col-xs-push-0 {
  left: auto;
}
.col-xs-offset-12 {
  margin-left: 100%;
}
.col-xs-offset-11 {
  margin-left: 91.66666667%;
}
.col-xs-offset-10 {
  margin-left: 83.33333333%;
}
.col-xs-offset-9 {
  margin-left: 75%;
}
.col-xs-offset-8 {
  margin-left: 66.66666667%;
}
.col-xs-offset-7 {
  margin-left: 58.33333333%;
}
.col-xs-offset-6 {
  margin-left: 50%;
}
.col-xs-offset-5 {
  margin-left: 41.66666667%;
}
.col-xs-offset-4 {
  margin-left: 33.33333333%;
}
.col-xs-offset-3 {
  margin-left: 25%;
}
.col-xs-offset-2 {
  margin-left: 16.66666667%;
}
.col-xs-offset-1 {
  margin-left: 8.33333333%;
}
.col-xs-offset-0 {
  margin-left: 0%;
}
@media (min-width: 768px) {
  .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12 {
    float: left;
  }
  .col-sm-12 {
    width: 100%;
  }
  .col-sm-11 {
    width: 91.66666667%;
  }
  .col-sm-10 {
    width: 83.33333333%;
  }
  .col-sm-9 {
    width: 75%;
  }
  .col-sm-8 {
    width: 66.66666667%;
  }
  .col-sm-7 {
    width: 58.33333333%;
  }
  .col-sm-6 {
    width: 50%;
  }
  .col-sm-5 {
    width: 41.66666667%;
  }
  .col-sm-4 {
    width: 33.33333333%;
  }
  .col-sm-3 {
    width: 25%;
  }
  .col-sm-2 {
    width: 16.66666667%;
  }
  .col-sm-1 {
    width: 8.33333333%;
  }
  .col-sm-pull-12 {
    right: 100%;
  }
  .col-sm-pull-11 {
    right: 91.66666667%;
  }
  .col-sm-pull-10 {
    right: 83.33333333%;
  }
  .col-sm-pull-9 {
    right: 75%;
  }
  .col-sm-pull-8 {
    right: 66.66666667%;
  }
  .col-sm-pull-7 {
    right: 58.33333333%;
  }
  .col-sm-pull-6 {
    right: 50%;
  }
  .col-sm-pull-5 {
    right: 41.66666667%;
  }
  .col-sm-pull-4 {
    right: 33.33333333%;
  }
  .col-sm-pull-3 {
    right: 25%;
  }
  .col-sm-pull-2 {
    right: 16.66666667%;
  }
  .col-sm-pull-1 {
    right: 8.33333333%;
  }
  .col-sm-pull-0 {
    right: auto;
  }
  .col-sm-push-12 {
    left: 100%;
  }
  .col-sm-push-11 {
    left: 91.66666667%;
  }
  .col-sm-push-10 {
    left: 83.33333333%;
  }
  .col-sm-push-9 {
    left: 75%;
  }
  .col-sm-push-8 {
    left: 66.66666667%;
  }
  .col-sm-push-7 {
    left: 58.33333333%;
  }
  .col-sm-push-6 {
    left: 50%;
  }
  .col-sm-push-5 {
    left: 41.66666667%;
  }
  .col-sm-push-4 {
    left: 33.33333333%;
  }
  .col-sm-push-3 {
    left: 25%;
  }
  .col-sm-push-2 {
    left: 16.66666667%;
  }
  .col-sm-push-1 {
    left: 8.33333333%;
  }
  .col-sm-push-0 {
    left: auto;
  }
  .col-sm-offset-12 {
    margin-left: 100%;
  }
  .col-sm-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-sm-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-sm-offset-9 {
    margin-left: 75%;
  }
  .col-sm-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-sm-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-sm-offset-6 {
    margin-left: 50%;
  }
  .col-sm-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-sm-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-sm-offset-3 {
    margin-left: 25%;
  }
  .col-sm-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-sm-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-sm-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 992px) {
  .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12 {
    float: left;
  }
  .col-md-12 {
    width: 100%;
  }
  .col-md-11 {
    width: 91.66666667%;
  }
  .col-md-10 {
    width: 83.33333333%;
  }
  .col-md-9 {
    width: 75%;
  }
  .col-md-8 {
    width: 66.66666667%;
  }
  .col-md-7 {
    width: 58.33333333%;
  }
  .col-md-6 {
    width: 50%;
  }
  .col-md-5 {
    width: 41.66666667%;
  }
  .col-md-4 {
    width: 33.33333333%;
  }
  .col-md-3 {
    width: 25%;
  }
  .col-md-2 {
    width: 16.66666667%;
  }
  .col-md-1 {
    width: 8.33333333%;
  }
  .col-md-pull-12 {
    right: 100%;
  }
  .col-md-pull-11 {
    right: 91.66666667%;
  }
  .col-md-pull-10 {
    right: 83.33333333%;
  }
  .col-md-pull-9 {
    right: 75%;
  }
  .col-md-pull-8 {
    right: 66.66666667%;
  }
  .col-md-pull-7 {
    right: 58.33333333%;
  }
  .col-md-pull-6 {
    right: 50%;
  }
  .col-md-pull-5 {
    right: 41.66666667%;
  }
  .col-md-pull-4 {
    right: 33.33333333%;
  }
  .col-md-pull-3 {
    right: 25%;
  }
  .col-md-pull-2 {
    right: 16.66666667%;
  }
  .col-md-pull-1 {
    right: 8.33333333%;
  }
  .col-md-pull-0 {
    right: auto;
  }
  .col-md-push-12 {
    left: 100%;
  }
  .col-md-push-11 {
    left: 91.66666667%;
  }
  .col-md-push-10 {
    left: 83.33333333%;
  }
  .col-md-push-9 {
    left: 75%;
  }
  .col-md-push-8 {
    left: 66.66666667%;
  }
  .col-md-push-7 {
    left: 58.33333333%;
  }
  .col-md-push-6 {
    left: 50%;
  }
  .col-md-push-5 {
    left: 41.66666667%;
  }
  .col-md-push-4 {
    left: 33.33333333%;
  }
  .col-md-push-3 {
    left: 25%;
  }
  .col-md-push-2 {
    left: 16.66666667%;
  }
  .col-md-push-1 {
    left: 8.33333333%;
  }
  .col-md-push-0 {
    left: auto;
  }
  .col-md-offset-12 {
    margin-left: 100%;
  }
  .col-md-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-md-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-md-offset-9 {
    margin-left: 75%;
  }
  .col-md-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-md-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-md-offset-6 {
    margin-left: 50%;
  }
  .col-md-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-md-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-md-offset-3 {
    margin-left: 25%;
  }
  .col-md-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-md-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-md-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 1200px) {
  .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12 {
    float: left;
  }
  .col-lg-12 {
    width: 100%;
  }
  .col-lg-11 {
    width: 91.66666667%;
  }
  .col-lg-10 {
    width: 83.33333333%;
  }
  .col-lg-9 {
    width: 75%;
  }
  .col-lg-8 {
    width: 66.66666667%;
  }
  .col-lg-7 {
    width: 58.33333333%;
  }
  .col-lg-6 {
    width: 50%;
  }
  .col-lg-5 {
    width: 41.66666667%;
  }
  .col-lg-4 {
    width: 33.33333333%;
  }
  .col-lg-3 {
    width: 25%;
  }
  .col-lg-2 {
    width: 16.66666667%;
  }
  .col-lg-1 {
    width: 8.33333333%;
  }
  .col-lg-pull-12 {
    right: 100%;
  }
  .col-lg-pull-11 {
    right: 91.66666667%;
  }
  .col-lg-pull-10 {
    right: 83.33333333%;
  }
  .col-lg-pull-9 {
    right: 75%;
  }
  .col-lg-pull-8 {
    right: 66.66666667%;
  }
  .col-lg-pull-7 {
    right: 58.33333333%;
  }
  .col-lg-pull-6 {
    right: 50%;
  }
  .col-lg-pull-5 {
    right: 41.66666667%;
  }
  .col-lg-pull-4 {
    right: 33.33333333%;
  }
  .col-lg-pull-3 {
    right: 25%;
  }
  .col-lg-pull-2 {
    right: 16.66666667%;
  }
  .col-lg-pull-1 {
    right: 8.33333333%;
  }
  .col-lg-pull-0 {
    right: auto;
  }
  .col-lg-push-12 {
    left: 100%;
  }
  .col-lg-push-11 {
    left: 91.66666667%;
  }
  .col-lg-push-10 {
    left: 83.33333333%;
  }
  .col-lg-push-9 {
    left: 75%;
  }
  .col-lg-push-8 {
    left: 66.66666667%;
  }
  .col-lg-push-7 {
    left: 58.33333333%;
  }
  .col-lg-push-6 {
    left: 50%;
  }
  .col-lg-push-5 {
    left: 41.66666667%;
  }
  .col-lg-push-4 {
    left: 33.33333333%;
  }
  .col-lg-push-3 {
    left: 25%;
  }
  .col-lg-push-2 {
    left: 16.66666667%;
  }
  .col-lg-push-1 {
    left: 8.33333333%;
  }
  .col-lg-push-0 {
    left: auto;
  }
  .col-lg-offset-12 {
    margin-left: 100%;
  }
  .col-lg-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-lg-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-lg-offset-9 {
    margin-left: 75%;
  }
  .col-lg-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-lg-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-lg-offset-6 {
    margin-left: 50%;
  }
  .col-lg-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-lg-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-lg-offset-3 {
    margin-left: 25%;
  }
  .col-lg-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-lg-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-lg-offset-0 {
    margin-left: 0%;
  }
}
table {
  background-color: transparent;
}
caption {
  padding-top: 8px;
  padding-bottom: 8px;
  color: #777777;
  text-align: left;
}
th {
  text-align: left;
}
.table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 18px;
}
.table > thead > tr > th,
.table > tbody > tr > th,
.table > tfoot > tr > th,
.table > thead > tr > td,
.table > tbody > tr > td,
.table > tfoot > tr > td {
  padding: 8px;
  line-height: 1.42857143;
  vertical-align: top;
  border-top: 1px solid #ddd;
}
.table > thead > tr > th {
  vertical-align: bottom;
  border-bottom: 2px solid #ddd;
}
.table > caption + thead > tr:first-child > th,
.table > colgroup + thead > tr:first-child > th,
.table > thead:first-child > tr:first-child > th,
.table > caption + thead > tr:first-child > td,
.table > colgroup + thead > tr:first-child > td,
.table > thead:first-child > tr:first-child > td {
  border-top: 0;
}
.table > tbody + tbody {
  border-top: 2px solid #ddd;
}
.table .table {
  background-color: #fff;
}
.table-condensed > thead > tr > th,
.table-condensed > tbody > tr > th,
.table-condensed > tfoot > tr > th,
.table-condensed > thead > tr > td,
.table-condensed > tbody > tr > td,
.table-condensed > tfoot > tr > td {
  padding: 5px;
}
.table-bordered {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > tbody > tr > th,
.table-bordered > tfoot > tr > th,
.table-bordered > thead > tr > td,
.table-bordered > tbody > tr > td,
.table-bordered > tfoot > tr > td {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > thead > tr > td {
  border-bottom-width: 2px;
}
.table-striped > tbody > tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}
.table-hover > tbody > tr:hover {
  background-color: #f5f5f5;
}
table col[class*="col-"] {
  position: static;
  float: none;
  display: table-column;
}
table td[class*="col-"],
table th[class*="col-"] {
  position: static;
  float: none;
  display: table-cell;
}
.table > thead > tr > td.active,
.table > tbody > tr > td.active,
.table > tfoot > tr > td.active,
.table > thead > tr > th.active,
.table > tbody > tr > th.active,
.table > tfoot > tr > th.active,
.table > thead > tr.active > td,
.table > tbody > tr.active > td,
.table > tfoot > tr.active > td,
.table > thead > tr.active > th,
.table > tbody > tr.active > th,
.table > tfoot > tr.active > th {
  background-color: #f5f5f5;
}
.table-hover > tbody > tr > td.active:hover,
.table-hover > tbody > tr > th.active:hover,
.table-hover > tbody > tr.active:hover > td,
.table-hover > tbody > tr:hover > .active,
.table-hover > tbody > tr.active:hover > th {
  background-color: #e8e8e8;
}
.table > thead > tr > td.success,
.table > tbody > tr > td.success,
.table > tfoot > tr > td.success,
.table > thead > tr > th.success,
.table > tbody > tr > th.success,
.table > tfoot > tr > th.success,
.table > thead > tr.success > td,
.table > tbody > tr.success > td,
.table > tfoot > tr.success > td,
.table > thead > tr.success > th,
.table > tbody > tr.success > th,
.table > tfoot > tr.success > th {
  background-color: #dff0d8;
}
.table-hover > tbody > tr > td.success:hover,
.table-hover > tbody > tr > th.success:hover,
.table-hover > tbody > tr.success:hover > td,
.table-hover > tbody > tr:hover > .success,
.table-hover > tbody > tr.success:hover > th {
  background-color: #d0e9c6;
}
.table > thead > tr > td.info,
.table > tbody > tr > td.info,
.table > tfoot > tr > td.info,
.table > thead > tr > th.info,
.table > tbody > tr > th.info,
.table > tfoot > tr > th.info,
.table > thead > tr.info > td,
.table > tbody > tr.info > td,
.table > tfoot > tr.info > td,
.table > thead > tr.info > th,
.table > tbody > tr.info > th,
.table > tfoot > tr.info > th {
  background-color: #d9edf7;
}
.table-hover > tbody > tr > td.info:hover,
.table-hover > tbody > tr > th.info:hover,
.table-hover > tbody > tr.info:hover > td,
.table-hover > tbody > tr:hover > .info,
.table-hover > tbody > tr.info:hover > th {
  background-color: #c4e3f3;
}
.table > thead > tr > td.warning,
.table > tbody > tr > td.warning,
.table > tfoot > tr > td.warning,
.table > thead > tr > th.warning,
.table > tbody > tr > th.warning,
.table > tfoot > tr > th.warning,
.table > thead > tr.warning > td,
.table > tbody > tr.warning > td,
.table > tfoot > tr.warning > td,
.table > thead > tr.warning > th,
.table > tbody > tr.warning > th,
.table > tfoot > tr.warning > th {
  background-color: #fcf8e3;
}
.table-hover > tbody > tr > td.warning:hover,
.table-hover > tbody > tr > th.warning:hover,
.table-hover > tbody > tr.warning:hover > td,
.table-hover > tbody > tr:hover > .warning,
.table-hover > tbody > tr.warning:hover > th {
  background-color: #faf2cc;
}
.table > thead > tr > td.danger,
.table > tbody > tr > td.danger,
.table > tfoot > tr > td.danger,
.table > thead > tr > th.danger,
.table > tbody > tr > th.danger,
.table > tfoot > tr > th.danger,
.table > thead > tr.danger > td,
.table > tbody > tr.danger > td,
.table > tfoot > tr.danger > td,
.table > thead > tr.danger > th,
.table > tbody > tr.danger > th,
.table > tfoot > tr.danger > th {
  background-color: #f2dede;
}
.table-hover > tbody > tr > td.danger:hover,
.table-hover > tbody > tr > th.danger:hover,
.table-hover > tbody > tr.danger:hover > td,
.table-hover > tbody > tr:hover > .danger,
.table-hover > tbody > tr.danger:hover > th {
  background-color: #ebcccc;
}
.table-responsive {
  overflow-x: auto;
  min-height: 0.01%;
}
@media screen and (max-width: 767px) {
  .table-responsive {
    width: 100%;
    margin-bottom: 13.5px;
    overflow-y: hidden;
    -ms-overflow-style: -ms-autohiding-scrollbar;
    border: 1px solid #ddd;
  }
  .table-responsive > .table {
    margin-bottom: 0;
  }
  .table-responsive > .table > thead > tr > th,
  .table-responsive > .table > tbody > tr > th,
  .table-responsive > .table > tfoot > tr > th,
  .table-responsive > .table > thead > tr > td,
  .table-responsive > .table > tbody > tr > td,
  .table-responsive > .table > tfoot > tr > td {
    white-space: nowrap;
  }
  .table-responsive > .table-bordered {
    border: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:first-child,
  .table-responsive > .table-bordered > tbody > tr > th:first-child,
  .table-responsive > .table-bordered > tfoot > tr > th:first-child,
  .table-responsive > .table-bordered > thead > tr > td:first-child,
  .table-responsive > .table-bordered > tbody > tr > td:first-child,
  .table-responsive > .table-bordered > tfoot > tr > td:first-child {
    border-left: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:last-child,
  .table-responsive > .table-bordered > tbody > tr > th:last-child,
  .table-responsive > .table-bordered > tfoot > tr > th:last-child,
  .table-responsive > .table-bordered > thead > tr > td:last-child,
  .table-responsive > .table-bordered > tbody > tr > td:last-child,
  .table-responsive > .table-bordered > tfoot > tr > td:last-child {
    border-right: 0;
  }
  .table-responsive > .table-bordered > tbody > tr:last-child > th,
  .table-responsive > .table-bordered > tfoot > tr:last-child > th,
  .table-responsive > .table-bordered > tbody > tr:last-child > td,
  .table-responsive > .table-bordered > tfoot > tr:last-child > td {
    border-bottom: 0;
  }
}
fieldset {
  padding: 0;
  margin: 0;
  border: 0;
  min-width: 0;
}
legend {
  display: block;
  width: 100%;
  padding: 0;
  margin-bottom: 18px;
  font-size: 19.5px;
  line-height: inherit;
  color: #333333;
  border: 0;
  border-bottom: 1px solid #e5e5e5;
}
label {
  display: inline-block;
  max-width: 100%;
  margin-bottom: 5px;
  font-weight: bold;
}
input[type="search"] {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
input[type="radio"],
input[type="checkbox"] {
  margin: 4px 0 0;
  margin-top: 1px \9;
  line-height: normal;
}
input[type="file"] {
  display: block;
}
input[type="range"] {
  display: block;
  width: 100%;
}
select[multiple],
select[size] {
  height: auto;
}
input[type="file"]:focus,
input[type="radio"]:focus,
input[type="checkbox"]:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
output {
  display: block;
  padding-top: 7px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
}
.form-control {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
}
.form-control:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.form-control::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.form-control:-ms-input-placeholder {
  color: #999;
}
.form-control::-webkit-input-placeholder {
  color: #999;
}
.form-control::-ms-expand {
  border: 0;
  background-color: transparent;
}
.form-control[disabled],
.form-control[readonly],
fieldset[disabled] .form-control {
  background-color: #eeeeee;
  opacity: 1;
}
.form-control[disabled],
fieldset[disabled] .form-control {
  cursor: not-allowed;
}
textarea.form-control {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: none;
}
@media screen and (-webkit-min-device-pixel-ratio: 0) {
  input[type="date"].form-control,
  input[type="time"].form-control,
  input[type="datetime-local"].form-control,
  input[type="month"].form-control {
    line-height: 32px;
  }
  input[type="date"].input-sm,
  input[type="time"].input-sm,
  input[type="datetime-local"].input-sm,
  input[type="month"].input-sm,
  .input-group-sm input[type="date"],
  .input-group-sm input[type="time"],
  .input-group-sm input[type="datetime-local"],
  .input-group-sm input[type="month"] {
    line-height: 30px;
  }
  input[type="date"].input-lg,
  input[type="time"].input-lg,
  input[type="datetime-local"].input-lg,
  input[type="month"].input-lg,
  .input-group-lg input[type="date"],
  .input-group-lg input[type="time"],
  .input-group-lg input[type="datetime-local"],
  .input-group-lg input[type="month"] {
    line-height: 45px;
  }
}
.form-group {
  margin-bottom: 15px;
}
.radio,
.checkbox {
  position: relative;
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
}
.radio label,
.checkbox label {
  min-height: 18px;
  padding-left: 20px;
  margin-bottom: 0;
  font-weight: normal;
  cursor: pointer;
}
.radio input[type="radio"],
.radio-inline input[type="radio"],
.checkbox input[type="checkbox"],
.checkbox-inline input[type="checkbox"] {
  position: absolute;
  margin-left: -20px;
  margin-top: 4px \9;
}
.radio + .radio,
.checkbox + .checkbox {
  margin-top: -5px;
}
.radio-inline,
.checkbox-inline {
  position: relative;
  display: inline-block;
  padding-left: 20px;
  margin-bottom: 0;
  vertical-align: middle;
  font-weight: normal;
  cursor: pointer;
}
.radio-inline + .radio-inline,
.checkbox-inline + .checkbox-inline {
  margin-top: 0;
  margin-left: 10px;
}
input[type="radio"][disabled],
input[type="checkbox"][disabled],
input[type="radio"].disabled,
input[type="checkbox"].disabled,
fieldset[disabled] input[type="radio"],
fieldset[disabled] input[type="checkbox"] {
  cursor: not-allowed;
}
.radio-inline.disabled,
.checkbox-inline.disabled,
fieldset[disabled] .radio-inline,
fieldset[disabled] .checkbox-inline {
  cursor: not-allowed;
}
.radio.disabled label,
.checkbox.disabled label,
fieldset[disabled] .radio label,
fieldset[disabled] .checkbox label {
  cursor: not-allowed;
}
.form-control-static {
  padding-top: 7px;
  padding-bottom: 7px;
  margin-bottom: 0;
  min-height: 31px;
}
.form-control-static.input-lg,
.form-control-static.input-sm {
  padding-left: 0;
  padding-right: 0;
}
.input-sm {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-sm {
  height: 30px;
  line-height: 30px;
}
textarea.input-sm,
select[multiple].input-sm {
  height: auto;
}
.form-group-sm .form-control {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.form-group-sm select.form-control {
  height: 30px;
  line-height: 30px;
}
.form-group-sm textarea.form-control,
.form-group-sm select[multiple].form-control {
  height: auto;
}
.form-group-sm .form-control-static {
  height: 30px;
  min-height: 30px;
  padding: 6px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.input-lg {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-lg {
  height: 45px;
  line-height: 45px;
}
textarea.input-lg,
select[multiple].input-lg {
  height: auto;
}
.form-group-lg .form-control {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.form-group-lg select.form-control {
  height: 45px;
  line-height: 45px;
}
.form-group-lg textarea.form-control,
.form-group-lg select[multiple].form-control {
  height: auto;
}
.form-group-lg .form-control-static {
  height: 45px;
  min-height: 35px;
  padding: 11px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.has-feedback {
  position: relative;
}
.has-feedback .form-control {
  padding-right: 40px;
}
.form-control-feedback {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 2;
  display: block;
  width: 32px;
  height: 32px;
  line-height: 32px;
  text-align: center;
  pointer-events: none;
}
.input-lg + .form-control-feedback,
.input-group-lg + .form-control-feedback,
.form-group-lg .form-control + .form-control-feedback {
  width: 45px;
  height: 45px;
  line-height: 45px;
}
.input-sm + .form-control-feedback,
.input-group-sm + .form-control-feedback,
.form-group-sm .form-control + .form-control-feedback {
  width: 30px;
  height: 30px;
  line-height: 30px;
}
.has-success .help-block,
.has-success .control-label,
.has-success .radio,
.has-success .checkbox,
.has-success .radio-inline,
.has-success .checkbox-inline,
.has-success.radio label,
.has-success.checkbox label,
.has-success.radio-inline label,
.has-success.checkbox-inline label {
  color: #3c763d;
}
.has-success .form-control {
  border-color: #3c763d;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-success .form-control:focus {
  border-color: #2b542c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
}
.has-success .input-group-addon {
  color: #3c763d;
  border-color: #3c763d;
  background-color: #dff0d8;
}
.has-success .form-control-feedback {
  color: #3c763d;
}
.has-warning .help-block,
.has-warning .control-label,
.has-warning .radio,
.has-warning .checkbox,
.has-warning .radio-inline,
.has-warning .checkbox-inline,
.has-warning.radio label,
.has-warning.checkbox label,
.has-warning.radio-inline label,
.has-warning.checkbox-inline label {
  color: #8a6d3b;
}
.has-warning .form-control {
  border-color: #8a6d3b;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-warning .form-control:focus {
  border-color: #66512c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
}
.has-warning .input-group-addon {
  color: #8a6d3b;
  border-color: #8a6d3b;
  background-color: #fcf8e3;
}
.has-warning .form-control-feedback {
  color: #8a6d3b;
}
.has-error .help-block,
.has-error .control-label,
.has-error .radio,
.has-error .checkbox,
.has-error .radio-inline,
.has-error .checkbox-inline,
.has-error.radio label,
.has-error.checkbox label,
.has-error.radio-inline label,
.has-error.checkbox-inline label {
  color: #a94442;
}
.has-error .form-control {
  border-color: #a94442;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-error .form-control:focus {
  border-color: #843534;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
}
.has-error .input-group-addon {
  color: #a94442;
  border-color: #a94442;
  background-color: #f2dede;
}
.has-error .form-control-feedback {
  color: #a94442;
}
.has-feedback label ~ .form-control-feedback {
  top: 23px;
}
.has-feedback label.sr-only ~ .form-control-feedback {
  top: 0;
}
.help-block {
  display: block;
  margin-top: 5px;
  margin-bottom: 10px;
  color: #404040;
}
@media (min-width: 768px) {
  .form-inline .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .form-inline .form-control-static {
    display: inline-block;
  }
  .form-inline .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .form-inline .input-group .input-group-addon,
  .form-inline .input-group .input-group-btn,
  .form-inline .input-group .form-control {
    width: auto;
  }
  .form-inline .input-group > .form-control {
    width: 100%;
  }
  .form-inline .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio,
  .form-inline .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio label,
  .form-inline .checkbox label {
    padding-left: 0;
  }
  .form-inline .radio input[type="radio"],
  .form-inline .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .form-inline .has-feedback .form-control-feedback {
    top: 0;
  }
}
.form-horizontal .radio,
.form-horizontal .checkbox,
.form-horizontal .radio-inline,
.form-horizontal .checkbox-inline {
  margin-top: 0;
  margin-bottom: 0;
  padding-top: 7px;
}
.form-horizontal .radio,
.form-horizontal .checkbox {
  min-height: 25px;
}
.form-horizontal .form-group {
  margin-left: 0px;
  margin-right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .control-label {
    text-align: right;
    margin-bottom: 0;
    padding-top: 7px;
  }
}
.form-horizontal .has-feedback .form-control-feedback {
  right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .form-group-lg .control-label {
    padding-top: 11px;
    font-size: 17px;
  }
}
@media (min-width: 768px) {
  .form-horizontal .form-group-sm .control-label {
    padding-top: 6px;
    font-size: 12px;
  }
}
.btn {
  display: inline-block;
  margin-bottom: 0;
  font-weight: normal;
  text-align: center;
  vertical-align: middle;
  touch-action: manipulation;
  cursor: pointer;
  background-image: none;
  border: 1px solid transparent;
  white-space: nowrap;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  border-radius: 2px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.btn:focus,
.btn:active:focus,
.btn.active:focus,
.btn.focus,
.btn:active.focus,
.btn.active.focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.btn:hover,
.btn:focus,
.btn.focus {
  color: #333;
  text-decoration: none;
}
.btn:active,
.btn.active {
  outline: 0;
  background-image: none;
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn.disabled,
.btn[disabled],
fieldset[disabled] .btn {
  cursor: not-allowed;
  opacity: 0.65;
  filter: alpha(opacity=65);
  -webkit-box-shadow: none;
  box-shadow: none;
}
a.btn.disabled,
fieldset[disabled] a.btn {
  pointer-events: none;
}
.btn-default {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.btn-default:focus,
.btn-default.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.btn-default:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active:hover,
.btn-default.active:hover,
.open > .dropdown-toggle.btn-default:hover,
.btn-default:active:focus,
.btn-default.active:focus,
.open > .dropdown-toggle.btn-default:focus,
.btn-default:active.focus,
.btn-default.active.focus,
.open > .dropdown-toggle.btn-default.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  background-image: none;
}
.btn-default.disabled:hover,
.btn-default[disabled]:hover,
fieldset[disabled] .btn-default:hover,
.btn-default.disabled:focus,
.btn-default[disabled]:focus,
fieldset[disabled] .btn-default:focus,
.btn-default.disabled.focus,
.btn-default[disabled].focus,
fieldset[disabled] .btn-default.focus {
  background-color: #fff;
  border-color: #ccc;
}
.btn-default .badge {
  color: #fff;
  background-color: #333;
}
.btn-primary {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary:focus,
.btn-primary.focus {
  color: #fff;
  background-color: #286090;
  border-color: #122b40;
}
.btn-primary:hover {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active:hover,
.btn-primary.active:hover,
.open > .dropdown-toggle.btn-primary:hover,
.btn-primary:active:focus,
.btn-primary.active:focus,
.open > .dropdown-toggle.btn-primary:focus,
.btn-primary:active.focus,
.btn-primary.active.focus,
.open > .dropdown-toggle.btn-primary.focus {
  color: #fff;
  background-color: #204d74;
  border-color: #122b40;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  background-image: none;
}
.btn-primary.disabled:hover,
.btn-primary[disabled]:hover,
fieldset[disabled] .btn-primary:hover,
.btn-primary.disabled:focus,
.btn-primary[disabled]:focus,
fieldset[disabled] .btn-primary:focus,
.btn-primary.disabled.focus,
.btn-primary[disabled].focus,
fieldset[disabled] .btn-primary.focus {
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary .badge {
  color: #337ab7;
  background-color: #fff;
}
.btn-success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success:focus,
.btn-success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.btn-success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active:hover,
.btn-success.active:hover,
.open > .dropdown-toggle.btn-success:hover,
.btn-success:active:focus,
.btn-success.active:focus,
.open > .dropdown-toggle.btn-success:focus,
.btn-success:active.focus,
.btn-success.active.focus,
.open > .dropdown-toggle.btn-success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  background-image: none;
}
.btn-success.disabled:hover,
.btn-success[disabled]:hover,
fieldset[disabled] .btn-success:hover,
.btn-success.disabled:focus,
.btn-success[disabled]:focus,
fieldset[disabled] .btn-success:focus,
.btn-success.disabled.focus,
.btn-success[disabled].focus,
fieldset[disabled] .btn-success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.btn-info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info:focus,
.btn-info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.btn-info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active:hover,
.btn-info.active:hover,
.open > .dropdown-toggle.btn-info:hover,
.btn-info:active:focus,
.btn-info.active:focus,
.open > .dropdown-toggle.btn-info:focus,
.btn-info:active.focus,
.btn-info.active.focus,
.open > .dropdown-toggle.btn-info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  background-image: none;
}
.btn-info.disabled:hover,
.btn-info[disabled]:hover,
fieldset[disabled] .btn-info:hover,
.btn-info.disabled:focus,
.btn-info[disabled]:focus,
fieldset[disabled] .btn-info:focus,
.btn-info.disabled.focus,
.btn-info[disabled].focus,
fieldset[disabled] .btn-info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.btn-warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning:focus,
.btn-warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.btn-warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active:hover,
.btn-warning.active:hover,
.open > .dropdown-toggle.btn-warning:hover,
.btn-warning:active:focus,
.btn-warning.active:focus,
.open > .dropdown-toggle.btn-warning:focus,
.btn-warning:active.focus,
.btn-warning.active.focus,
.open > .dropdown-toggle.btn-warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  background-image: none;
}
.btn-warning.disabled:hover,
.btn-warning[disabled]:hover,
fieldset[disabled] .btn-warning:hover,
.btn-warning.disabled:focus,
.btn-warning[disabled]:focus,
fieldset[disabled] .btn-warning:focus,
.btn-warning.disabled.focus,
.btn-warning[disabled].focus,
fieldset[disabled] .btn-warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.btn-danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger:focus,
.btn-danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.btn-danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active:hover,
.btn-danger.active:hover,
.open > .dropdown-toggle.btn-danger:hover,
.btn-danger:active:focus,
.btn-danger.active:focus,
.open > .dropdown-toggle.btn-danger:focus,
.btn-danger:active.focus,
.btn-danger.active.focus,
.open > .dropdown-toggle.btn-danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  background-image: none;
}
.btn-danger.disabled:hover,
.btn-danger[disabled]:hover,
fieldset[disabled] .btn-danger:hover,
.btn-danger.disabled:focus,
.btn-danger[disabled]:focus,
fieldset[disabled] .btn-danger:focus,
.btn-danger.disabled.focus,
.btn-danger[disabled].focus,
fieldset[disabled] .btn-danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger .badge {
  color: #d9534f;
  background-color: #fff;
}
.btn-link {
  color: #337ab7;
  font-weight: normal;
  border-radius: 0;
}
.btn-link,
.btn-link:active,
.btn-link.active,
.btn-link[disabled],
fieldset[disabled] .btn-link {
  background-color: transparent;
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn-link,
.btn-link:hover,
.btn-link:focus,
.btn-link:active {
  border-color: transparent;
}
.btn-link:hover,
.btn-link:focus {
  color: #23527c;
  text-decoration: underline;
  background-color: transparent;
}
.btn-link[disabled]:hover,
fieldset[disabled] .btn-link:hover,
.btn-link[disabled]:focus,
fieldset[disabled] .btn-link:focus {
  color: #777777;
  text-decoration: none;
}
.btn-lg,
.btn-group-lg > .btn {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.btn-sm,
.btn-group-sm > .btn {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-xs,
.btn-group-xs > .btn {
  padding: 1px 5px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-block {
  display: block;
  width: 100%;
}
.btn-block + .btn-block {
  margin-top: 5px;
}
input[type="submit"].btn-block,
input[type="reset"].btn-block,
input[type="button"].btn-block {
  width: 100%;
}
.fade {
  opacity: 0;
  -webkit-transition: opacity 0.15s linear;
  -o-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
}
.fade.in {
  opacity: 1;
}
.collapse {
  display: none;
}
.collapse.in {
  display: block;
}
tr.collapse.in {
  display: table-row;
}
tbody.collapse.in {
  display: table-row-group;
}
.collapsing {
  position: relative;
  height: 0;
  overflow: hidden;
  -webkit-transition-property: height, visibility;
  transition-property: height, visibility;
  -webkit-transition-duration: 0.35s;
  transition-duration: 0.35s;
  -webkit-transition-timing-function: ease;
  transition-timing-function: ease;
}
.caret {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 2px;
  vertical-align: middle;
  border-top: 4px dashed;
  border-top: 4px solid \9;
  border-right: 4px solid transparent;
  border-left: 4px solid transparent;
}
.dropup,
.dropdown {
  position: relative;
}
.dropdown-toggle:focus {
  outline: 0;
}
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  float: left;
  min-width: 160px;
  padding: 5px 0;
  margin: 2px 0 0;
  list-style: none;
  font-size: 13px;
  text-align: left;
  background-color: #fff;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 2px;
  -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  background-clip: padding-box;
}
.dropdown-menu.pull-right {
  right: 0;
  left: auto;
}
.dropdown-menu .divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.dropdown-menu > li > a {
  display: block;
  padding: 3px 20px;
  clear: both;
  font-weight: normal;
  line-height: 1.42857143;
  color: #333333;
  white-space: nowrap;
}
.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus {
  text-decoration: none;
  color: #262626;
  background-color: #f5f5f5;
}
.dropdown-menu > .active > a,
.dropdown-menu > .active > a:hover,
.dropdown-menu > .active > a:focus {
  color: #fff;
  text-decoration: none;
  outline: 0;
  background-color: #337ab7;
}
.dropdown-menu > .disabled > a,
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  color: #777777;
}
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  text-decoration: none;
  background-color: transparent;
  background-image: none;
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  cursor: not-allowed;
}
.open > .dropdown-menu {
  display: block;
}
.open > a {
  outline: 0;
}
.dropdown-menu-right {
  left: auto;
  right: 0;
}
.dropdown-menu-left {
  left: 0;
  right: auto;
}
.dropdown-header {
  display: block;
  padding: 3px 20px;
  font-size: 12px;
  line-height: 1.42857143;
  color: #777777;
  white-space: nowrap;
}
.dropdown-backdrop {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  z-index: 990;
}
.pull-right > .dropdown-menu {
  right: 0;
  left: auto;
}
.dropup .caret,
.navbar-fixed-bottom .dropdown .caret {
  border-top: 0;
  border-bottom: 4px dashed;
  border-bottom: 4px solid \9;
  content: "";
}
.dropup .dropdown-menu,
.navbar-fixed-bottom .dropdown .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-bottom: 2px;
}
@media (min-width: 541px) {
  .navbar-right .dropdown-menu {
    left: auto;
    right: 0;
  }
  .navbar-right .dropdown-menu-left {
    left: 0;
    right: auto;
  }
}
.btn-group,
.btn-group-vertical {
  position: relative;
  display: inline-block;
  vertical-align: middle;
}
.btn-group > .btn,
.btn-group-vertical > .btn {
  position: relative;
  float: left;
}
.btn-group > .btn:hover,
.btn-group-vertical > .btn:hover,
.btn-group > .btn:focus,
.btn-group-vertical > .btn:focus,
.btn-group > .btn:active,
.btn-group-vertical > .btn:active,
.btn-group > .btn.active,
.btn-group-vertical > .btn.active {
  z-index: 2;
}
.btn-group .btn + .btn,
.btn-group .btn + .btn-group,
.btn-group .btn-group + .btn,
.btn-group .btn-group + .btn-group {
  margin-left: -1px;
}
.btn-toolbar {
  margin-left: -5px;
}
.btn-toolbar .btn,
.btn-toolbar .btn-group,
.btn-toolbar .input-group {
  float: left;
}
.btn-toolbar > .btn,
.btn-toolbar > .btn-group,
.btn-toolbar > .input-group {
  margin-left: 5px;
}
.btn-group > .btn:not(:first-child):not(:last-child):not(.dropdown-toggle) {
  border-radius: 0;
}
.btn-group > .btn:first-child {
  margin-left: 0;
}
.btn-group > .btn:first-child:not(:last-child):not(.dropdown-toggle) {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn:last-child:not(:first-child),
.btn-group > .dropdown-toggle:not(:first-child) {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group > .btn-group {
  float: left;
}
.btn-group > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group .dropdown-toggle:active,
.btn-group.open .dropdown-toggle {
  outline: 0;
}
.btn-group > .btn + .dropdown-toggle {
  padding-left: 8px;
  padding-right: 8px;
}
.btn-group > .btn-lg + .dropdown-toggle {
  padding-left: 12px;
  padding-right: 12px;
}
.btn-group.open .dropdown-toggle {
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn-group.open .dropdown-toggle.btn-link {
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn .caret {
  margin-left: 0;
}
.btn-lg .caret {
  border-width: 5px 5px 0;
  border-bottom-width: 0;
}
.dropup .btn-lg .caret {
  border-width: 0 5px 5px;
}
.btn-group-vertical > .btn,
.btn-group-vertical > .btn-group,
.btn-group-vertical > .btn-group > .btn {
  display: block;
  float: none;
  width: 100%;
  max-width: 100%;
}
.btn-group-vertical > .btn-group > .btn {
  float: none;
}
.btn-group-vertical > .btn + .btn,
.btn-group-vertical > .btn + .btn-group,
.btn-group-vertical > .btn-group + .btn,
.btn-group-vertical > .btn-group + .btn-group {
  margin-top: -1px;
  margin-left: 0;
}
.btn-group-vertical > .btn:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.btn-group-vertical > .btn:first-child:not(:last-child) {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn:last-child:not(:first-child) {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
.btn-group-vertical > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.btn-group-justified {
  display: table;
  width: 100%;
  table-layout: fixed;
  border-collapse: separate;
}
.btn-group-justified > .btn,
.btn-group-justified > .btn-group {
  float: none;
  display: table-cell;
  width: 1%;
}
.btn-group-justified > .btn-group .btn {
  width: 100%;
}
.btn-group-justified > .btn-group .dropdown-menu {
  left: auto;
}
[data-toggle="buttons"] > .btn input[type="radio"],
[data-toggle="buttons"] > .btn-group > .btn input[type="radio"],
[data-toggle="buttons"] > .btn input[type="checkbox"],
[data-toggle="buttons"] > .btn-group > .btn input[type="checkbox"] {
  position: absolute;
  clip: rect(0, 0, 0, 0);
  pointer-events: none;
}
.input-group {
  position: relative;
  display: table;
  border-collapse: separate;
}
.input-group[class*="col-"] {
  float: none;
  padding-left: 0;
  padding-right: 0;
}
.input-group .form-control {
  position: relative;
  z-index: 2;
  float: left;
  width: 100%;
  margin-bottom: 0;
}
.input-group .form-control:focus {
  z-index: 3;
}
.input-group-lg > .form-control,
.input-group-lg > .input-group-addon,
.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-group-lg > .form-control,
select.input-group-lg > .input-group-addon,
select.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  line-height: 45px;
}
textarea.input-group-lg > .form-control,
textarea.input-group-lg > .input-group-addon,
textarea.input-group-lg > .input-group-btn > .btn,
select[multiple].input-group-lg > .form-control,
select[multiple].input-group-lg > .input-group-addon,
select[multiple].input-group-lg > .input-group-btn > .btn {
  height: auto;
}
.input-group-sm > .form-control,
.input-group-sm > .input-group-addon,
.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-group-sm > .form-control,
select.input-group-sm > .input-group-addon,
select.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  line-height: 30px;
}
textarea.input-group-sm > .form-control,
textarea.input-group-sm > .input-group-addon,
textarea.input-group-sm > .input-group-btn > .btn,
select[multiple].input-group-sm > .form-control,
select[multiple].input-group-sm > .input-group-addon,
select[multiple].input-group-sm > .input-group-btn > .btn {
  height: auto;
}
.input-group-addon,
.input-group-btn,
.input-group .form-control {
  display: table-cell;
}
.input-group-addon:not(:first-child):not(:last-child),
.input-group-btn:not(:first-child):not(:last-child),
.input-group .form-control:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.input-group-addon,
.input-group-btn {
  width: 1%;
  white-space: nowrap;
  vertical-align: middle;
}
.input-group-addon {
  padding: 6px 12px;
  font-size: 13px;
  font-weight: normal;
  line-height: 1;
  color: #555555;
  text-align: center;
  background-color: #eeeeee;
  border: 1px solid #ccc;
  border-radius: 2px;
}
.input-group-addon.input-sm {
  padding: 5px 10px;
  font-size: 12px;
  border-radius: 1px;
}
.input-group-addon.input-lg {
  padding: 10px 16px;
  font-size: 17px;
  border-radius: 3px;
}
.input-group-addon input[type="radio"],
.input-group-addon input[type="checkbox"] {
  margin-top: 0;
}
.input-group .form-control:first-child,
.input-group-addon:first-child,
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group > .btn,
.input-group-btn:first-child > .dropdown-toggle,
.input-group-btn:last-child > .btn:not(:last-child):not(.dropdown-toggle),
.input-group-btn:last-child > .btn-group:not(:last-child) > .btn {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.input-group-addon:first-child {
  border-right: 0;
}
.input-group .form-control:last-child,
.input-group-addon:last-child,
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group > .btn,
.input-group-btn:last-child > .dropdown-toggle,
.input-group-btn:first-child > .btn:not(:first-child),
.input-group-btn:first-child > .btn-group:not(:first-child) > .btn {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.input-group-addon:last-child {
  border-left: 0;
}
.input-group-btn {
  position: relative;
  font-size: 0;
  white-space: nowrap;
}
.input-group-btn > .btn {
  position: relative;
}
.input-group-btn > .btn + .btn {
  margin-left: -1px;
}
.input-group-btn > .btn:hover,
.input-group-btn > .btn:focus,
.input-group-btn > .btn:active {
  z-index: 2;
}
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group {
  margin-right: -1px;
}
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group {
  z-index: 2;
  margin-left: -1px;
}
.nav {
  margin-bottom: 0;
  padding-left: 0;
  list-style: none;
}
.nav > li {
  position: relative;
  display: block;
}
.nav > li > a {
  position: relative;
  display: block;
  padding: 10px 15px;
}
.nav > li > a:hover,
.nav > li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.nav > li.disabled > a {
  color: #777777;
}
.nav > li.disabled > a:hover,
.nav > li.disabled > a:focus {
  color: #777777;
  text-decoration: none;
  background-color: transparent;
  cursor: not-allowed;
}
.nav .open > a,
.nav .open > a:hover,
.nav .open > a:focus {
  background-color: #eeeeee;
  border-color: #337ab7;
}
.nav .nav-divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.nav > li > a > img {
  max-width: none;
}
.nav-tabs {
  border-bottom: 1px solid #ddd;
}
.nav-tabs > li {
  float: left;
  margin-bottom: -1px;
}
.nav-tabs > li > a {
  margin-right: 2px;
  line-height: 1.42857143;
  border: 1px solid transparent;
  border-radius: 2px 2px 0 0;
}
.nav-tabs > li > a:hover {
  border-color: #eeeeee #eeeeee #ddd;
}
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a:focus {
  color: #555555;
  background-color: #fff;
  border: 1px solid #ddd;
  border-bottom-color: transparent;
  cursor: default;
}
.nav-tabs.nav-justified {
  width: 100%;
  border-bottom: 0;
}
.nav-tabs.nav-justified > li {
  float: none;
}
.nav-tabs.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-tabs.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-tabs.nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs.nav-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs.nav-justified > .active > a,
.nav-tabs.nav-justified > .active > a:hover,
.nav-tabs.nav-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs.nav-justified > .active > a,
  .nav-tabs.nav-justified > .active > a:hover,
  .nav-tabs.nav-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.nav-pills > li {
  float: left;
}
.nav-pills > li > a {
  border-radius: 2px;
}
.nav-pills > li + li {
  margin-left: 2px;
}
.nav-pills > li.active > a,
.nav-pills > li.active > a:hover,
.nav-pills > li.active > a:focus {
  color: #fff;
  background-color: #337ab7;
}
.nav-stacked > li {
  float: none;
}
.nav-stacked > li + li {
  margin-top: 2px;
  margin-left: 0;
}
.nav-justified {
  width: 100%;
}
.nav-justified > li {
  float: none;
}
.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs-justified {
  border-bottom: 0;
}
.nav-tabs-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs-justified > .active > a,
.nav-tabs-justified > .active > a:hover,
.nav-tabs-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs-justified > .active > a,
  .nav-tabs-justified > .active > a:hover,
  .nav-tabs-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.tab-content > .tab-pane {
  display: none;
}
.tab-content > .active {
  display: block;
}
.nav-tabs .dropdown-menu {
  margin-top: -1px;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar {
  position: relative;
  min-height: 30px;
  margin-bottom: 18px;
  border: 1px solid transparent;
}
@media (min-width: 541px) {
  .navbar {
    border-radius: 2px;
  }
}
@media (min-width: 541px) {
  .navbar-header {
    float: left;
  }
}
.navbar-collapse {
  overflow-x: visible;
  padding-right: 0px;
  padding-left: 0px;
  border-top: 1px solid transparent;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
  -webkit-overflow-scrolling: touch;
}
.navbar-collapse.in {
  overflow-y: auto;
}
@media (min-width: 541px) {
  .navbar-collapse {
    width: auto;
    border-top: 0;
    box-shadow: none;
  }
  .navbar-collapse.collapse {
    display: block !important;
    height: auto !important;
    padding-bottom: 0;
    overflow: visible !important;
  }
  .navbar-collapse.in {
    overflow-y: visible;
  }
  .navbar-fixed-top .navbar-collapse,
  .navbar-static-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    padding-left: 0;
    padding-right: 0;
  }
}
.navbar-fixed-top .navbar-collapse,
.navbar-fixed-bottom .navbar-collapse {
  max-height: 340px;
}
@media (max-device-width: 540px) and (orientation: landscape) {
  .navbar-fixed-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    max-height: 200px;
  }
}
.container > .navbar-header,
.container-fluid > .navbar-header,
.container > .navbar-collapse,
.container-fluid > .navbar-collapse {
  margin-right: 0px;
  margin-left: 0px;
}
@media (min-width: 541px) {
  .container > .navbar-header,
  .container-fluid > .navbar-header,
  .container > .navbar-collapse,
  .container-fluid > .navbar-collapse {
    margin-right: 0;
    margin-left: 0;
  }
}
.navbar-static-top {
  z-index: 1000;
  border-width: 0 0 1px;
}
@media (min-width: 541px) {
  .navbar-static-top {
    border-radius: 0;
  }
}
.navbar-fixed-top,
.navbar-fixed-bottom {
  position: fixed;
  right: 0;
  left: 0;
  z-index: 1030;
}
@media (min-width: 541px) {
  .navbar-fixed-top,
  .navbar-fixed-bottom {
    border-radius: 0;
  }
}
.navbar-fixed-top {
  top: 0;
  border-width: 0 0 1px;
}
.navbar-fixed-bottom {
  bottom: 0;
  margin-bottom: 0;
  border-width: 1px 0 0;
}
.navbar-brand {
  float: left;
  padding: 6px 0px;
  font-size: 17px;
  line-height: 18px;
  height: 30px;
}
.navbar-brand:hover,
.navbar-brand:focus {
  text-decoration: none;
}
.navbar-brand > img {
  display: block;
}
@media (min-width: 541px) {
  .navbar > .container .navbar-brand,
  .navbar > .container-fluid .navbar-brand {
    margin-left: 0px;
  }
}
.navbar-toggle {
  position: relative;
  float: right;
  margin-right: 0px;
  padding: 9px 10px;
  margin-top: -2px;
  margin-bottom: -2px;
  background-color: transparent;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 2px;
}
.navbar-toggle:focus {
  outline: 0;
}
.navbar-toggle .icon-bar {
  display: block;
  width: 22px;
  height: 2px;
  border-radius: 1px;
}
.navbar-toggle .icon-bar + .icon-bar {
  margin-top: 4px;
}
@media (min-width: 541px) {
  .navbar-toggle {
    display: none;
  }
}
.navbar-nav {
  margin: 3px 0px;
}
.navbar-nav > li > a {
  padding-top: 10px;
  padding-bottom: 10px;
  line-height: 18px;
}
@media (max-width: 540px) {
  .navbar-nav .open .dropdown-menu {
    position: static;
    float: none;
    width: auto;
    margin-top: 0;
    background-color: transparent;
    border: 0;
    box-shadow: none;
  }
  .navbar-nav .open .dropdown-menu > li > a,
  .navbar-nav .open .dropdown-menu .dropdown-header {
    padding: 5px 15px 5px 25px;
  }
  .navbar-nav .open .dropdown-menu > li > a {
    line-height: 18px;
  }
  .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-nav .open .dropdown-menu > li > a:focus {
    background-image: none;
  }
}
@media (min-width: 541px) {
  .navbar-nav {
    float: left;
    margin: 0;
  }
  .navbar-nav > li {
    float: left;
  }
  .navbar-nav > li > a {
    padding-top: 6px;
    padding-bottom: 6px;
  }
}
.navbar-form {
  margin-left: 0px;
  margin-right: 0px;
  padding: 10px 0px;
  border-top: 1px solid transparent;
  border-bottom: 1px solid transparent;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  margin-top: -1px;
  margin-bottom: -1px;
}
@media (min-width: 768px) {
  .navbar-form .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .navbar-form .form-control-static {
    display: inline-block;
  }
  .navbar-form .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .navbar-form .input-group .input-group-addon,
  .navbar-form .input-group .input-group-btn,
  .navbar-form .input-group .form-control {
    width: auto;
  }
  .navbar-form .input-group > .form-control {
    width: 100%;
  }
  .navbar-form .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio,
  .navbar-form .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio label,
  .navbar-form .checkbox label {
    padding-left: 0;
  }
  .navbar-form .radio input[type="radio"],
  .navbar-form .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .navbar-form .has-feedback .form-control-feedback {
    top: 0;
  }
}
@media (max-width: 540px) {
  .navbar-form .form-group {
    margin-bottom: 5px;
  }
  .navbar-form .form-group:last-child {
    margin-bottom: 0;
  }
}
@media (min-width: 541px) {
  .navbar-form {
    width: auto;
    border: 0;
    margin-left: 0;
    margin-right: 0;
    padding-top: 0;
    padding-bottom: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
  }
}
.navbar-nav > li > .dropdown-menu {
  margin-top: 0;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar-fixed-bottom .navbar-nav > li > .dropdown-menu {
  margin-bottom: 0;
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.navbar-btn {
  margin-top: -1px;
  margin-bottom: -1px;
}
.navbar-btn.btn-sm {
  margin-top: 0px;
  margin-bottom: 0px;
}
.navbar-btn.btn-xs {
  margin-top: 4px;
  margin-bottom: 4px;
}
.navbar-text {
  margin-top: 6px;
  margin-bottom: 6px;
}
@media (min-width: 541px) {
  .navbar-text {
    float: left;
    margin-left: 0px;
    margin-right: 0px;
  }
}
@media (min-width: 541px) {
  .navbar-left {
    float: left !important;
    float: left;
  }
  .navbar-right {
    float: right !important;
    float: right;
    margin-right: 0px;
  }
  .navbar-right ~ .navbar-right {
    margin-right: 0;
  }
}
.navbar-default {
  background-color: #f8f8f8;
  border-color: #e7e7e7;
}
.navbar-default .navbar-brand {
  color: #777;
}
.navbar-default .navbar-brand:hover,
.navbar-default .navbar-brand:focus {
  color: #5e5e5e;
  background-color: transparent;
}
.navbar-default .navbar-text {
  color: #777;
}
.navbar-default .navbar-nav > li > a {
  color: #777;
}
.navbar-default .navbar-nav > li > a:hover,
.navbar-default .navbar-nav > li > a:focus {
  color: #333;
  background-color: transparent;
}
.navbar-default .navbar-nav > .active > a,
.navbar-default .navbar-nav > .active > a:hover,
.navbar-default .navbar-nav > .active > a:focus {
  color: #555;
  background-color: #e7e7e7;
}
.navbar-default .navbar-nav > .disabled > a,
.navbar-default .navbar-nav > .disabled > a:hover,
.navbar-default .navbar-nav > .disabled > a:focus {
  color: #ccc;
  background-color: transparent;
}
.navbar-default .navbar-toggle {
  border-color: #ddd;
}
.navbar-default .navbar-toggle:hover,
.navbar-default .navbar-toggle:focus {
  background-color: #ddd;
}
.navbar-default .navbar-toggle .icon-bar {
  background-color: #888;
}
.navbar-default .navbar-collapse,
.navbar-default .navbar-form {
  border-color: #e7e7e7;
}
.navbar-default .navbar-nav > .open > a,
.navbar-default .navbar-nav > .open > a:hover,
.navbar-default .navbar-nav > .open > a:focus {
  background-color: #e7e7e7;
  color: #555;
}
@media (max-width: 540px) {
  .navbar-default .navbar-nav .open .dropdown-menu > li > a {
    color: #777;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #333;
    background-color: transparent;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #555;
    background-color: #e7e7e7;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #ccc;
    background-color: transparent;
  }
}
.navbar-default .navbar-link {
  color: #777;
}
.navbar-default .navbar-link:hover {
  color: #333;
}
.navbar-default .btn-link {
  color: #777;
}
.navbar-default .btn-link:hover,
.navbar-default .btn-link:focus {
  color: #333;
}
.navbar-default .btn-link[disabled]:hover,
fieldset[disabled] .navbar-default .btn-link:hover,
.navbar-default .btn-link[disabled]:focus,
fieldset[disabled] .navbar-default .btn-link:focus {
  color: #ccc;
}
.navbar-inverse {
  background-color: #222;
  border-color: #080808;
}
.navbar-inverse .navbar-brand {
  color: #9d9d9d;
}
.navbar-inverse .navbar-brand:hover,
.navbar-inverse .navbar-brand:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-text {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a:hover,
.navbar-inverse .navbar-nav > li > a:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-nav > .active > a,
.navbar-inverse .navbar-nav > .active > a:hover,
.navbar-inverse .navbar-nav > .active > a:focus {
  color: #fff;
  background-color: #080808;
}
.navbar-inverse .navbar-nav > .disabled > a,
.navbar-inverse .navbar-nav > .disabled > a:hover,
.navbar-inverse .navbar-nav > .disabled > a:focus {
  color: #444;
  background-color: transparent;
}
.navbar-inverse .navbar-toggle {
  border-color: #333;
}
.navbar-inverse .navbar-toggle:hover,
.navbar-inverse .navbar-toggle:focus {
  background-color: #333;
}
.navbar-inverse .navbar-toggle .icon-bar {
  background-color: #fff;
}
.navbar-inverse .navbar-collapse,
.navbar-inverse .navbar-form {
  border-color: #101010;
}
.navbar-inverse .navbar-nav > .open > a,
.navbar-inverse .navbar-nav > .open > a:hover,
.navbar-inverse .navbar-nav > .open > a:focus {
  background-color: #080808;
  color: #fff;
}
@media (max-width: 540px) {
  .navbar-inverse .navbar-nav .open .dropdown-menu > .dropdown-header {
    border-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu .divider {
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a {
    color: #9d9d9d;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #fff;
    background-color: transparent;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #fff;
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #444;
    background-color: transparent;
  }
}
.navbar-inverse .navbar-link {
  color: #9d9d9d;
}
.navbar-inverse .navbar-link:hover {
  color: #fff;
}
.navbar-inverse .btn-link {
  color: #9d9d9d;
}
.navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link:focus {
  color: #fff;
}
.navbar-inverse .btn-link[disabled]:hover,
fieldset[disabled] .navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link[disabled]:focus,
fieldset[disabled] .navbar-inverse .btn-link:focus {
  color: #444;
}
.breadcrumb {
  padding: 8px 15px;
  margin-bottom: 18px;
  list-style: none;
  background-color: #f5f5f5;
  border-radius: 2px;
}
.breadcrumb > li {
  display: inline-block;
}
.breadcrumb > li + li:before {
  content: "/\00a0";
  padding: 0 5px;
  color: #5e5e5e;
}
.breadcrumb > .active {
  color: #777777;
}
.pagination {
  display: inline-block;
  padding-left: 0;
  margin: 18px 0;
  border-radius: 2px;
}
.pagination > li {
  display: inline;
}
.pagination > li > a,
.pagination > li > span {
  position: relative;
  float: left;
  padding: 6px 12px;
  line-height: 1.42857143;
  text-decoration: none;
  color: #337ab7;
  background-color: #fff;
  border: 1px solid #ddd;
  margin-left: -1px;
}
.pagination > li:first-child > a,
.pagination > li:first-child > span {
  margin-left: 0;
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.pagination > li:last-child > a,
.pagination > li:last-child > span {
  border-bottom-right-radius: 2px;
  border-top-right-radius: 2px;
}
.pagination > li > a:hover,
.pagination > li > span:hover,
.pagination > li > a:focus,
.pagination > li > span:focus {
  z-index: 2;
  color: #23527c;
  background-color: #eeeeee;
  border-color: #ddd;
}
.pagination > .active > a,
.pagination > .active > span,
.pagination > .active > a:hover,
.pagination > .active > span:hover,
.pagination > .active > a:focus,
.pagination > .active > span:focus {
  z-index: 3;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
  cursor: default;
}
.pagination > .disabled > span,
.pagination > .disabled > span:hover,
.pagination > .disabled > span:focus,
.pagination > .disabled > a,
.pagination > .disabled > a:hover,
.pagination > .disabled > a:focus {
  color: #777777;
  background-color: #fff;
  border-color: #ddd;
  cursor: not-allowed;
}
.pagination-lg > li > a,
.pagination-lg > li > span {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.pagination-lg > li:first-child > a,
.pagination-lg > li:first-child > span {
  border-bottom-left-radius: 3px;
  border-top-left-radius: 3px;
}
.pagination-lg > li:last-child > a,
.pagination-lg > li:last-child > span {
  border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
}
.pagination-sm > li > a,
.pagination-sm > li > span {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.pagination-sm > li:first-child > a,
.pagination-sm > li:first-child > span {
  border-bottom-left-radius: 1px;
  border-top-left-radius: 1px;
}
.pagination-sm > li:last-child > a,
.pagination-sm > li:last-child > span {
  border-bottom-right-radius: 1px;
  border-top-right-radius: 1px;
}
.pager {
  padding-left: 0;
  margin: 18px 0;
  list-style: none;
  text-align: center;
}
.pager li {
  display: inline;
}
.pager li > a,
.pager li > span {
  display: inline-block;
  padding: 5px 14px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 15px;
}
.pager li > a:hover,
.pager li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.pager .next > a,
.pager .next > span {
  float: right;
}
.pager .previous > a,
.pager .previous > span {
  float: left;
}
.pager .disabled > a,
.pager .disabled > a:hover,
.pager .disabled > a:focus,
.pager .disabled > span {
  color: #777777;
  background-color: #fff;
  cursor: not-allowed;
}
.label {
  display: inline;
  padding: .2em .6em .3em;
  font-size: 75%;
  font-weight: bold;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .25em;
}
a.label:hover,
a.label:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.label:empty {
  display: none;
}
.btn .label {
  position: relative;
  top: -1px;
}
.label-default {
  background-color: #777777;
}
.label-default[href]:hover,
.label-default[href]:focus {
  background-color: #5e5e5e;
}
.label-primary {
  background-color: #337ab7;
}
.label-primary[href]:hover,
.label-primary[href]:focus {
  background-color: #286090;
}
.label-success {
  background-color: #5cb85c;
}
.label-success[href]:hover,
.label-success[href]:focus {
  background-color: #449d44;
}
.label-info {
  background-color: #5bc0de;
}
.label-info[href]:hover,
.label-info[href]:focus {
  background-color: #31b0d5;
}
.label-warning {
  background-color: #f0ad4e;
}
.label-warning[href]:hover,
.label-warning[href]:focus {
  background-color: #ec971f;
}
.label-danger {
  background-color: #d9534f;
}
.label-danger[href]:hover,
.label-danger[href]:focus {
  background-color: #c9302c;
}
.badge {
  display: inline-block;
  min-width: 10px;
  padding: 3px 7px;
  font-size: 12px;
  font-weight: bold;
  color: #fff;
  line-height: 1;
  vertical-align: middle;
  white-space: nowrap;
  text-align: center;
  background-color: #777777;
  border-radius: 10px;
}
.badge:empty {
  display: none;
}
.btn .badge {
  position: relative;
  top: -1px;
}
.btn-xs .badge,
.btn-group-xs > .btn .badge {
  top: 0;
  padding: 1px 5px;
}
a.badge:hover,
a.badge:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.list-group-item.active > .badge,
.nav-pills > .active > a > .badge {
  color: #337ab7;
  background-color: #fff;
}
.list-group-item > .badge {
  float: right;
}
.list-group-item > .badge + .badge {
  margin-right: 5px;
}
.nav-pills > li > a > .badge {
  margin-left: 3px;
}
.jumbotron {
  padding-top: 30px;
  padding-bottom: 30px;
  margin-bottom: 30px;
  color: inherit;
  background-color: #eeeeee;
}
.jumbotron h1,
.jumbotron .h1 {
  color: inherit;
}
.jumbotron p {
  margin-bottom: 15px;
  font-size: 20px;
  font-weight: 200;
}
.jumbotron > hr {
  border-top-color: #d5d5d5;
}
.container .jumbotron,
.container-fluid .jumbotron {
  border-radius: 3px;
  padding-left: 0px;
  padding-right: 0px;
}
.jumbotron .container {
  max-width: 100%;
}
@media screen and (min-width: 768px) {
  .jumbotron {
    padding-top: 48px;
    padding-bottom: 48px;
  }
  .container .jumbotron,
  .container-fluid .jumbotron {
    padding-left: 60px;
    padding-right: 60px;
  }
  .jumbotron h1,
  .jumbotron .h1 {
    font-size: 59px;
  }
}
.thumbnail {
  display: block;
  padding: 4px;
  margin-bottom: 18px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: border 0.2s ease-in-out;
  -o-transition: border 0.2s ease-in-out;
  transition: border 0.2s ease-in-out;
}
.thumbnail > img,
.thumbnail a > img {
  margin-left: auto;
  margin-right: auto;
}
a.thumbnail:hover,
a.thumbnail:focus,
a.thumbnail.active {
  border-color: #337ab7;
}
.thumbnail .caption {
  padding: 9px;
  color: #000;
}
.alert {
  padding: 15px;
  margin-bottom: 18px;
  border: 1px solid transparent;
  border-radius: 2px;
}
.alert h4 {
  margin-top: 0;
  color: inherit;
}
.alert .alert-link {
  font-weight: bold;
}
.alert > p,
.alert > ul {
  margin-bottom: 0;
}
.alert > p + p {
  margin-top: 5px;
}
.alert-dismissable,
.alert-dismissible {
  padding-right: 35px;
}
.alert-dismissable .close,
.alert-dismissible .close {
  position: relative;
  top: -2px;
  right: -21px;
  color: inherit;
}
.alert-success {
  background-color: #dff0d8;
  border-color: #d6e9c6;
  color: #3c763d;
}
.alert-success hr {
  border-top-color: #c9e2b3;
}
.alert-success .alert-link {
  color: #2b542c;
}
.alert-info {
  background-color: #d9edf7;
  border-color: #bce8f1;
  color: #31708f;
}
.alert-info hr {
  border-top-color: #a6e1ec;
}
.alert-info .alert-link {
  color: #245269;
}
.alert-warning {
  background-color: #fcf8e3;
  border-color: #faebcc;
  color: #8a6d3b;
}
.alert-warning hr {
  border-top-color: #f7e1b5;
}
.alert-warning .alert-link {
  color: #66512c;
}
.alert-danger {
  background-color: #f2dede;
  border-color: #ebccd1;
  color: #a94442;
}
.alert-danger hr {
  border-top-color: #e4b9c0;
}
.alert-danger .alert-link {
  color: #843534;
}
@-webkit-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
@keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
.progress {
  overflow: hidden;
  height: 18px;
  margin-bottom: 18px;
  background-color: #f5f5f5;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
}
.progress-bar {
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 18px;
  color: #fff;
  text-align: center;
  background-color: #337ab7;
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -webkit-transition: width 0.6s ease;
  -o-transition: width 0.6s ease;
  transition: width 0.6s ease;
}
.progress-striped .progress-bar,
.progress-bar-striped {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-size: 40px 40px;
}
.progress.active .progress-bar,
.progress-bar.active {
  -webkit-animation: progress-bar-stripes 2s linear infinite;
  -o-animation: progress-bar-stripes 2s linear infinite;
  animation: progress-bar-stripes 2s linear infinite;
}
.progress-bar-success {
  background-color: #5cb85c;
}
.progress-striped .progress-bar-success {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-info {
  background-color: #5bc0de;
}
.progress-striped .progress-bar-info {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-warning {
  background-color: #f0ad4e;
}
.progress-striped .progress-bar-warning {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-danger {
  background-color: #d9534f;
}
.progress-striped .progress-bar-danger {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.media {
  margin-top: 15px;
}
.media:first-child {
  margin-top: 0;
}
.media,
.media-body {
  zoom: 1;
  overflow: hidden;
}
.media-body {
  width: 10000px;
}
.media-object {
  display: block;
}
.media-object.img-thumbnail {
  max-width: none;
}
.media-right,
.media > .pull-right {
  padding-left: 10px;
}
.media-left,
.media > .pull-left {
  padding-right: 10px;
}
.media-left,
.media-right,
.media-body {
  display: table-cell;
  vertical-align: top;
}
.media-middle {
  vertical-align: middle;
}
.media-bottom {
  vertical-align: bottom;
}
.media-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.media-list {
  padding-left: 0;
  list-style: none;
}
.list-group {
  margin-bottom: 20px;
  padding-left: 0;
}
.list-group-item {
  position: relative;
  display: block;
  padding: 10px 15px;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid #ddd;
}
.list-group-item:first-child {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
}
.list-group-item:last-child {
  margin-bottom: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
a.list-group-item,
button.list-group-item {
  color: #555;
}
a.list-group-item .list-group-item-heading,
button.list-group-item .list-group-item-heading {
  color: #333;
}
a.list-group-item:hover,
button.list-group-item:hover,
a.list-group-item:focus,
button.list-group-item:focus {
  text-decoration: none;
  color: #555;
  background-color: #f5f5f5;
}
button.list-group-item {
  width: 100%;
  text-align: left;
}
.list-group-item.disabled,
.list-group-item.disabled:hover,
.list-group-item.disabled:focus {
  background-color: #eeeeee;
  color: #777777;
  cursor: not-allowed;
}
.list-group-item.disabled .list-group-item-heading,
.list-group-item.disabled:hover .list-group-item-heading,
.list-group-item.disabled:focus .list-group-item-heading {
  color: inherit;
}
.list-group-item.disabled .list-group-item-text,
.list-group-item.disabled:hover .list-group-item-text,
.list-group-item.disabled:focus .list-group-item-text {
  color: #777777;
}
.list-group-item.active,
.list-group-item.active:hover,
.list-group-item.active:focus {
  z-index: 2;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.list-group-item.active .list-group-item-heading,
.list-group-item.active:hover .list-group-item-heading,
.list-group-item.active:focus .list-group-item-heading,
.list-group-item.active .list-group-item-heading > small,
.list-group-item.active:hover .list-group-item-heading > small,
.list-group-item.active:focus .list-group-item-heading > small,
.list-group-item.active .list-group-item-heading > .small,
.list-group-item.active:hover .list-group-item-heading > .small,
.list-group-item.active:focus .list-group-item-heading > .small {
  color: inherit;
}
.list-group-item.active .list-group-item-text,
.list-group-item.active:hover .list-group-item-text,
.list-group-item.active:focus .list-group-item-text {
  color: #c7ddef;
}
.list-group-item-success {
  color: #3c763d;
  background-color: #dff0d8;
}
a.list-group-item-success,
button.list-group-item-success {
  color: #3c763d;
}
a.list-group-item-success .list-group-item-heading,
button.list-group-item-success .list-group-item-heading {
  color: inherit;
}
a.list-group-item-success:hover,
button.list-group-item-success:hover,
a.list-group-item-success:focus,
button.list-group-item-success:focus {
  color: #3c763d;
  background-color: #d0e9c6;
}
a.list-group-item-success.active,
button.list-group-item-success.active,
a.list-group-item-success.active:hover,
button.list-group-item-success.active:hover,
a.list-group-item-success.active:focus,
button.list-group-item-success.active:focus {
  color: #fff;
  background-color: #3c763d;
  border-color: #3c763d;
}
.list-group-item-info {
  color: #31708f;
  background-color: #d9edf7;
}
a.list-group-item-info,
button.list-group-item-info {
  color: #31708f;
}
a.list-group-item-info .list-group-item-heading,
button.list-group-item-info .list-group-item-heading {
  color: inherit;
}
a.list-group-item-info:hover,
button.list-group-item-info:hover,
a.list-group-item-info:focus,
button.list-group-item-info:focus {
  color: #31708f;
  background-color: #c4e3f3;
}
a.list-group-item-info.active,
button.list-group-item-info.active,
a.list-group-item-info.active:hover,
button.list-group-item-info.active:hover,
a.list-group-item-info.active:focus,
button.list-group-item-info.active:focus {
  color: #fff;
  background-color: #31708f;
  border-color: #31708f;
}
.list-group-item-warning {
  color: #8a6d3b;
  background-color: #fcf8e3;
}
a.list-group-item-warning,
button.list-group-item-warning {
  color: #8a6d3b;
}
a.list-group-item-warning .list-group-item-heading,
button.list-group-item-warning .list-group-item-heading {
  color: inherit;
}
a.list-group-item-warning:hover,
button.list-group-item-warning:hover,
a.list-group-item-warning:focus,
button.list-group-item-warning:focus {
  color: #8a6d3b;
  background-color: #faf2cc;
}
a.list-group-item-warning.active,
button.list-group-item-warning.active,
a.list-group-item-warning.active:hover,
button.list-group-item-warning.active:hover,
a.list-group-item-warning.active:focus,
button.list-group-item-warning.active:focus {
  color: #fff;
  background-color: #8a6d3b;
  border-color: #8a6d3b;
}
.list-group-item-danger {
  color: #a94442;
  background-color: #f2dede;
}
a.list-group-item-danger,
button.list-group-item-danger {
  color: #a94442;
}
a.list-group-item-danger .list-group-item-heading,
button.list-group-item-danger .list-group-item-heading {
  color: inherit;
}
a.list-group-item-danger:hover,
button.list-group-item-danger:hover,
a.list-group-item-danger:focus,
button.list-group-item-danger:focus {
  color: #a94442;
  background-color: #ebcccc;
}
a.list-group-item-danger.active,
button.list-group-item-danger.active,
a.list-group-item-danger.active:hover,
button.list-group-item-danger.active:hover,
a.list-group-item-danger.active:focus,
button.list-group-item-danger.active:focus {
  color: #fff;
  background-color: #a94442;
  border-color: #a94442;
}
.list-group-item-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.list-group-item-text {
  margin-bottom: 0;
  line-height: 1.3;
}
.panel {
  margin-bottom: 18px;
  background-color: #fff;
  border: 1px solid transparent;
  border-radius: 2px;
  -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
}
.panel-body {
  padding: 15px;
}
.panel-heading {
  padding: 10px 15px;
  border-bottom: 1px solid transparent;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel-heading > .dropdown .dropdown-toggle {
  color: inherit;
}
.panel-title {
  margin-top: 0;
  margin-bottom: 0;
  font-size: 15px;
  color: inherit;
}
.panel-title > a,
.panel-title > small,
.panel-title > .small,
.panel-title > small > a,
.panel-title > .small > a {
  color: inherit;
}
.panel-footer {
  padding: 10px 15px;
  background-color: #f5f5f5;
  border-top: 1px solid #ddd;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .list-group,
.panel > .panel-collapse > .list-group {
  margin-bottom: 0;
}
.panel > .list-group .list-group-item,
.panel > .panel-collapse > .list-group .list-group-item {
  border-width: 1px 0;
  border-radius: 0;
}
.panel > .list-group:first-child .list-group-item:first-child,
.panel > .panel-collapse > .list-group:first-child .list-group-item:first-child {
  border-top: 0;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .list-group:last-child .list-group-item:last-child,
.panel > .panel-collapse > .list-group:last-child .list-group-item:last-child {
  border-bottom: 0;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .panel-heading + .panel-collapse > .list-group .list-group-item:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.panel-heading + .list-group .list-group-item:first-child {
  border-top-width: 0;
}
.list-group + .panel-footer {
  border-top-width: 0;
}
.panel > .table,
.panel > .table-responsive > .table,
.panel > .panel-collapse > .table {
  margin-bottom: 0;
}
.panel > .table caption,
.panel > .table-responsive > .table caption,
.panel > .panel-collapse > .table caption {
  padding-left: 15px;
  padding-right: 15px;
}
.panel > .table:first-child,
.panel > .table-responsive:first-child > .table:first-child {
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child {
  border-top-left-radius: 1px;
  border-top-right-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:first-child {
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:last-child {
  border-top-right-radius: 1px;
}
.panel > .table:last-child,
.panel > .table-responsive:last-child > .table:last-child {
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child {
  border-bottom-left-radius: 1px;
  border-bottom-right-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:first-child {
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:last-child {
  border-bottom-right-radius: 1px;
}
.panel > .panel-body + .table,
.panel > .panel-body + .table-responsive,
.panel > .table + .panel-body,
.panel > .table-responsive + .panel-body {
  border-top: 1px solid #ddd;
}
.panel > .table > tbody:first-child > tr:first-child th,
.panel > .table > tbody:first-child > tr:first-child td {
  border-top: 0;
}
.panel > .table-bordered,
.panel > .table-responsive > .table-bordered {
  border: 0;
}
.panel > .table-bordered > thead > tr > th:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:first-child,
.panel > .table-bordered > tbody > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:first-child,
.panel > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-bordered > thead > tr > td:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:first-child,
.panel > .table-bordered > tbody > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:first-child,
.panel > .table-bordered > tfoot > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:first-child {
  border-left: 0;
}
.panel > .table-bordered > thead > tr > th:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:last-child,
.panel > .table-bordered > tbody > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:last-child,
.panel > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-bordered > thead > tr > td:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:last-child,
.panel > .table-bordered > tbody > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:last-child,
.panel > .table-bordered > tfoot > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:last-child {
  border-right: 0;
}
.panel > .table-bordered > thead > tr:first-child > td,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > td,
.panel > .table-bordered > tbody > tr:first-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > td,
.panel > .table-bordered > thead > tr:first-child > th,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > th,
.panel > .table-bordered > tbody > tr:first-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > th {
  border-bottom: 0;
}
.panel > .table-bordered > tbody > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > td,
.panel > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-bordered > tbody > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > th,
.panel > .table-bordered > tfoot > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > th {
  border-bottom: 0;
}
.panel > .table-responsive {
  border: 0;
  margin-bottom: 0;
}
.panel-group {
  margin-bottom: 18px;
}
.panel-group .panel {
  margin-bottom: 0;
  border-radius: 2px;
}
.panel-group .panel + .panel {
  margin-top: 5px;
}
.panel-group .panel-heading {
  border-bottom: 0;
}
.panel-group .panel-heading + .panel-collapse > .panel-body,
.panel-group .panel-heading + .panel-collapse > .list-group {
  border-top: 1px solid #ddd;
}
.panel-group .panel-footer {
  border-top: 0;
}
.panel-group .panel-footer + .panel-collapse .panel-body {
  border-bottom: 1px solid #ddd;
}
.panel-default {
  border-color: #ddd;
}
.panel-default > .panel-heading {
  color: #333333;
  background-color: #f5f5f5;
  border-color: #ddd;
}
.panel-default > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ddd;
}
.panel-default > .panel-heading .badge {
  color: #f5f5f5;
  background-color: #333333;
}
.panel-default > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ddd;
}
.panel-primary {
  border-color: #337ab7;
}
.panel-primary > .panel-heading {
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.panel-primary > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #337ab7;
}
.panel-primary > .panel-heading .badge {
  color: #337ab7;
  background-color: #fff;
}
.panel-primary > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #337ab7;
}
.panel-success {
  border-color: #d6e9c6;
}
.panel-success > .panel-heading {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}
.panel-success > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #d6e9c6;
}
.panel-success > .panel-heading .badge {
  color: #dff0d8;
  background-color: #3c763d;
}
.panel-success > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #d6e9c6;
}
.panel-info {
  border-color: #bce8f1;
}
.panel-info > .panel-heading {
  color: #31708f;
  background-color: #d9edf7;
  border-color: #bce8f1;
}
.panel-info > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #bce8f1;
}
.panel-info > .panel-heading .badge {
  color: #d9edf7;
  background-color: #31708f;
}
.panel-info > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #bce8f1;
}
.panel-warning {
  border-color: #faebcc;
}
.panel-warning > .panel-heading {
  color: #8a6d3b;
  background-color: #fcf8e3;
  border-color: #faebcc;
}
.panel-warning > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #faebcc;
}
.panel-warning > .panel-heading .badge {
  color: #fcf8e3;
  background-color: #8a6d3b;
}
.panel-warning > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #faebcc;
}
.panel-danger {
  border-color: #ebccd1;
}
.panel-danger > .panel-heading {
  color: #a94442;
  background-color: #f2dede;
  border-color: #ebccd1;
}
.panel-danger > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ebccd1;
}
.panel-danger > .panel-heading .badge {
  color: #f2dede;
  background-color: #a94442;
}
.panel-danger > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ebccd1;
}
.embed-responsive {
  position: relative;
  display: block;
  height: 0;
  padding: 0;
  overflow: hidden;
}
.embed-responsive .embed-responsive-item,
.embed-responsive iframe,
.embed-responsive embed,
.embed-responsive object,
.embed-responsive video {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  height: 100%;
  width: 100%;
  border: 0;
}
.embed-responsive-16by9 {
  padding-bottom: 56.25%;
}
.embed-responsive-4by3 {
  padding-bottom: 75%;
}
.well {
  min-height: 20px;
  padding: 19px;
  margin-bottom: 20px;
  background-color: #f5f5f5;
  border: 1px solid #e3e3e3;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
}
.well blockquote {
  border-color: #ddd;
  border-color: rgba(0, 0, 0, 0.15);
}
.well-lg {
  padding: 24px;
  border-radius: 3px;
}
.well-sm {
  padding: 9px;
  border-radius: 1px;
}
.close {
  float: right;
  font-size: 19.5px;
  font-weight: bold;
  line-height: 1;
  color: #000;
  text-shadow: 0 1px 0 #fff;
  opacity: 0.2;
  filter: alpha(opacity=20);
}
.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
  opacity: 0.5;
  filter: alpha(opacity=50);
}
button.close {
  padding: 0;
  cursor: pointer;
  background: transparent;
  border: 0;
  -webkit-appearance: none;
}
.modal-open {
  overflow: hidden;
}
.modal {
  display: none;
  overflow: hidden;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1050;
  -webkit-overflow-scrolling: touch;
  outline: 0;
}
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, -25%);
  -ms-transform: translate(0, -25%);
  -o-transform: translate(0, -25%);
  transform: translate(0, -25%);
  -webkit-transition: -webkit-transform 0.3s ease-out;
  -moz-transition: -moz-transform 0.3s ease-out;
  -o-transition: -o-transform 0.3s ease-out;
  transition: transform 0.3s ease-out;
}
.modal.in .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
.modal-open .modal {
  overflow-x: hidden;
  overflow-y: auto;
}
.modal-dialog {
  position: relative;
  width: auto;
  margin: 10px;
}
.modal-content {
  position: relative;
  background-color: #fff;
  border: 1px solid #999;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  background-clip: padding-box;
  outline: 0;
}
.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1040;
  background-color: #000;
}
.modal-backdrop.fade {
  opacity: 0;
  filter: alpha(opacity=0);
}
.modal-backdrop.in {
  opacity: 0.5;
  filter: alpha(opacity=50);
}
.modal-header {
  padding: 15px;
  border-bottom: 1px solid #e5e5e5;
}
.modal-header .close {
  margin-top: -2px;
}
.modal-title {
  margin: 0;
  line-height: 1.42857143;
}
.modal-body {
  position: relative;
  padding: 15px;
}
.modal-footer {
  padding: 15px;
  text-align: right;
  border-top: 1px solid #e5e5e5;
}
.modal-footer .btn + .btn {
  margin-left: 5px;
  margin-bottom: 0;
}
.modal-footer .btn-group .btn + .btn {
  margin-left: -1px;
}
.modal-footer .btn-block + .btn-block {
  margin-left: 0;
}
.modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll;
}
@media (min-width: 768px) {
  .modal-dialog {
    width: 600px;
    margin: 30px auto;
  }
  .modal-content {
    -webkit-box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  }
  .modal-sm {
    width: 300px;
  }
}
@media (min-width: 992px) {
  .modal-lg {
    width: 900px;
  }
}
.tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 12px;
  opacity: 0;
  filter: alpha(opacity=0);
}
.tooltip.in {
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.tooltip.top {
  margin-top: -3px;
  padding: 5px 0;
}
.tooltip.right {
  margin-left: 3px;
  padding: 0 5px;
}
.tooltip.bottom {
  margin-top: 3px;
  padding: 5px 0;
}
.tooltip.left {
  margin-left: -3px;
  padding: 0 5px;
}
.tooltip-inner {
  max-width: 200px;
  padding: 3px 8px;
  color: #fff;
  text-align: center;
  background-color: #000;
  border-radius: 2px;
}
.tooltip-arrow {
  position: absolute;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.tooltip.top .tooltip-arrow {
  bottom: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-left .tooltip-arrow {
  bottom: 0;
  right: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-right .tooltip-arrow {
  bottom: 0;
  left: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.right .tooltip-arrow {
  top: 50%;
  left: 0;
  margin-top: -5px;
  border-width: 5px 5px 5px 0;
  border-right-color: #000;
}
.tooltip.left .tooltip-arrow {
  top: 50%;
  right: 0;
  margin-top: -5px;
  border-width: 5px 0 5px 5px;
  border-left-color: #000;
}
.tooltip.bottom .tooltip-arrow {
  top: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-left .tooltip-arrow {
  top: 0;
  right: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-right .tooltip-arrow {
  top: 0;
  left: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.popover {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1060;
  display: none;
  max-width: 276px;
  padding: 1px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 13px;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}
.popover.top {
  margin-top: -10px;
}
.popover.right {
  margin-left: 10px;
}
.popover.bottom {
  margin-top: 10px;
}
.popover.left {
  margin-left: -10px;
}
.popover-title {
  margin: 0;
  padding: 8px 14px;
  font-size: 13px;
  background-color: #f7f7f7;
  border-bottom: 1px solid #ebebeb;
  border-radius: 2px 2px 0 0;
}
.popover-content {
  padding: 9px 14px;
}
.popover > .arrow,
.popover > .arrow:after {
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.popover > .arrow {
  border-width: 11px;
}
.popover > .arrow:after {
  border-width: 10px;
  content: "";
}
.popover.top > .arrow {
  left: 50%;
  margin-left: -11px;
  border-bottom-width: 0;
  border-top-color: #999999;
  border-top-color: rgba(0, 0, 0, 0.25);
  bottom: -11px;
}
.popover.top > .arrow:after {
  content: " ";
  bottom: 1px;
  margin-left: -10px;
  border-bottom-width: 0;
  border-top-color: #fff;
}
.popover.right > .arrow {
  top: 50%;
  left: -11px;
  margin-top: -11px;
  border-left-width: 0;
  border-right-color: #999999;
  border-right-color: rgba(0, 0, 0, 0.25);
}
.popover.right > .arrow:after {
  content: " ";
  left: 1px;
  bottom: -10px;
  border-left-width: 0;
  border-right-color: #fff;
}
.popover.bottom > .arrow {
  left: 50%;
  margin-left: -11px;
  border-top-width: 0;
  border-bottom-color: #999999;
  border-bottom-color: rgba(0, 0, 0, 0.25);
  top: -11px;
}
.popover.bottom > .arrow:after {
  content: " ";
  top: 1px;
  margin-left: -10px;
  border-top-width: 0;
  border-bottom-color: #fff;
}
.popover.left > .arrow {
  top: 50%;
  right: -11px;
  margin-top: -11px;
  border-right-width: 0;
  border-left-color: #999999;
  border-left-color: rgba(0, 0, 0, 0.25);
}
.popover.left > .arrow:after {
  content: " ";
  right: 1px;
  border-right-width: 0;
  border-left-color: #fff;
  bottom: -10px;
}
.carousel {
  position: relative;
}
.carousel-inner {
  position: relative;
  overflow: hidden;
  width: 100%;
}
.carousel-inner > .item {
  display: none;
  position: relative;
  -webkit-transition: 0.6s ease-in-out left;
  -o-transition: 0.6s ease-in-out left;
  transition: 0.6s ease-in-out left;
}
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  line-height: 1;
}
@media all and (transform-3d), (-webkit-transform-3d) {
  .carousel-inner > .item {
    -webkit-transition: -webkit-transform 0.6s ease-in-out;
    -moz-transition: -moz-transform 0.6s ease-in-out;
    -o-transition: -o-transform 0.6s ease-in-out;
    transition: transform 0.6s ease-in-out;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-perspective: 1000px;
    -moz-perspective: 1000px;
    perspective: 1000px;
  }
  .carousel-inner > .item.next,
  .carousel-inner > .item.active.right {
    -webkit-transform: translate3d(100%, 0, 0);
    transform: translate3d(100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.prev,
  .carousel-inner > .item.active.left {
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.next.left,
  .carousel-inner > .item.prev.right,
  .carousel-inner > .item.active {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    left: 0;
  }
}
.carousel-inner > .active,
.carousel-inner > .next,
.carousel-inner > .prev {
  display: block;
}
.carousel-inner > .active {
  left: 0;
}
.carousel-inner > .next,
.carousel-inner > .prev {
  position: absolute;
  top: 0;
  width: 100%;
}
.carousel-inner > .next {
  left: 100%;
}
.carousel-inner > .prev {
  left: -100%;
}
.carousel-inner > .next.left,
.carousel-inner > .prev.right {
  left: 0;
}
.carousel-inner > .active.left {
  left: -100%;
}
.carousel-inner > .active.right {
  left: 100%;
}
.carousel-control {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 15%;
  opacity: 0.5;
  filter: alpha(opacity=50);
  font-size: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
  background-color: rgba(0, 0, 0, 0);
}
.carousel-control.left {
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#80000000', endColorstr='#00000000', GradientType=1);
}
.carousel-control.right {
  left: auto;
  right: 0;
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#00000000', endColorstr='#80000000', GradientType=1);
}
.carousel-control:hover,
.carousel-control:focus {
  outline: 0;
  color: #fff;
  text-decoration: none;
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.carousel-control .icon-prev,
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-left,
.carousel-control .glyphicon-chevron-right {
  position: absolute;
  top: 50%;
  margin-top: -10px;
  z-index: 5;
  display: inline-block;
}
.carousel-control .icon-prev,
.carousel-control .glyphicon-chevron-left {
  left: 50%;
  margin-left: -10px;
}
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-right {
  right: 50%;
  margin-right: -10px;
}
.carousel-control .icon-prev,
.carousel-control .icon-next {
  width: 20px;
  height: 20px;
  line-height: 1;
  font-family: serif;
}
.carousel-control .icon-prev:before {
  content: '\2039';
}
.carousel-control .icon-next:before {
  content: '\203a';
}
.carousel-indicators {
  position: absolute;
  bottom: 10px;
  left: 50%;
  z-index: 15;
  width: 60%;
  margin-left: -30%;
  padding-left: 0;
  list-style: none;
  text-align: center;
}
.carousel-indicators li {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin: 1px;
  text-indent: -999px;
  border: 1px solid #fff;
  border-radius: 10px;
  cursor: pointer;
  background-color: #000 \9;
  background-color: rgba(0, 0, 0, 0);
}
.carousel-indicators .active {
  margin: 0;
  width: 12px;
  height: 12px;
  background-color: #fff;
}
.carousel-caption {
  position: absolute;
  left: 15%;
  right: 15%;
  bottom: 20px;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
}
.carousel-caption .btn {
  text-shadow: none;
}
@media screen and (min-width: 768px) {
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-prev,
  .carousel-control .icon-next {
    width: 30px;
    height: 30px;
    margin-top: -10px;
    font-size: 30px;
  }
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .icon-prev {
    margin-left: -10px;
  }
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-next {
    margin-right: -10px;
  }
  .carousel-caption {
    left: 20%;
    right: 20%;
    padding-bottom: 30px;
  }
  .carousel-indicators {
    bottom: 20px;
  }
}
.clearfix:before,
.clearfix:after,
.dl-horizontal dd:before,
.dl-horizontal dd:after,
.container:before,
.container:after,
.container-fluid:before,
.container-fluid:after,
.row:before,
.row:after,
.form-horizontal .form-group:before,
.form-horizontal .form-group:after,
.btn-toolbar:before,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:before,
.btn-group-vertical > .btn-group:after,
.nav:before,
.nav:after,
.navbar:before,
.navbar:after,
.navbar-header:before,
.navbar-header:after,
.navbar-collapse:before,
.navbar-collapse:after,
.pager:before,
.pager:after,
.panel-body:before,
.panel-body:after,
.modal-header:before,
.modal-header:after,
.modal-footer:before,
.modal-footer:after,
.item_buttons:before,
.item_buttons:after {
  content: " ";
  display: table;
}
.clearfix:after,
.dl-horizontal dd:after,
.container:after,
.container-fluid:after,
.row:after,
.form-horizontal .form-group:after,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:after,
.nav:after,
.navbar:after,
.navbar-header:after,
.navbar-collapse:after,
.pager:after,
.panel-body:after,
.modal-header:after,
.modal-footer:after,
.item_buttons:after {
  clear: both;
}
.center-block {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.pull-right {
  float: right !important;
}
.pull-left {
  float: left !important;
}
.hide {
  display: none !important;
}
.show {
  display: block !important;
}
.invisible {
  visibility: hidden;
}
.text-hide {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}
.hidden {
  display: none !important;
}
.affix {
  position: fixed;
}
@-ms-viewport {
  width: device-width;
}
.visible-xs,
.visible-sm,
.visible-md,
.visible-lg {
  display: none !important;
}
.visible-xs-block,
.visible-xs-inline,
.visible-xs-inline-block,
.visible-sm-block,
.visible-sm-inline,
.visible-sm-inline-block,
.visible-md-block,
.visible-md-inline,
.visible-md-inline-block,
.visible-lg-block,
.visible-lg-inline,
.visible-lg-inline-block {
  display: none !important;
}
@media (max-width: 767px) {
  .visible-xs {
    display: block !important;
  }
  table.visible-xs {
    display: table !important;
  }
  tr.visible-xs {
    display: table-row !important;
  }
  th.visible-xs,
  td.visible-xs {
    display: table-cell !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-block {
    display: block !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline {
    display: inline !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm {
    display: block !important;
  }
  table.visible-sm {
    display: table !important;
  }
  tr.visible-sm {
    display: table-row !important;
  }
  th.visible-sm,
  td.visible-sm {
    display: table-cell !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-block {
    display: block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline {
    display: inline !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md {
    display: block !important;
  }
  table.visible-md {
    display: table !important;
  }
  tr.visible-md {
    display: table-row !important;
  }
  th.visible-md,
  td.visible-md {
    display: table-cell !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-block {
    display: block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline {
    display: inline !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg {
    display: block !important;
  }
  table.visible-lg {
    display: table !important;
  }
  tr.visible-lg {
    display: table-row !important;
  }
  th.visible-lg,
  td.visible-lg {
    display: table-cell !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-block {
    display: block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline {
    display: inline !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline-block {
    display: inline-block !important;
  }
}
@media (max-width: 767px) {
  .hidden-xs {
    display: none !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .hidden-sm {
    display: none !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .hidden-md {
    display: none !important;
  }
}
@media (min-width: 1200px) {
  .hidden-lg {
    display: none !important;
  }
}
.visible-print {
  display: none !important;
}
@media print {
  .visible-print {
    display: block !important;
  }
  table.visible-print {
    display: table !important;
  }
  tr.visible-print {
    display: table-row !important;
  }
  th.visible-print,
  td.visible-print {
    display: table-cell !important;
  }
}
.visible-print-block {
  display: none !important;
}
@media print {
  .visible-print-block {
    display: block !important;
  }
}
.visible-print-inline {
  display: none !important;
}
@media print {
  .visible-print-inline {
    display: inline !important;
  }
}
.visible-print-inline-block {
  display: none !important;
}
@media print {
  .visible-print-inline-block {
    display: inline-block !important;
  }
}
@media print {
  .hidden-print {
    display: none !important;
  }
}
/*!
*
* Font Awesome
*
*/
/*!
 *  Font Awesome 4.7.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */
/* FONT PATH
 * -------------------------- */
@font-face {
  font-family: 'FontAwesome';
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?v=4.7.0');
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?#iefix&v=4.7.0') format('embedded-opentype'), url('../components/font-awesome/fonts/fontawesome-webfont.woff2?v=4.7.0') format('woff2'), url('../components/font-awesome/fonts/fontawesome-webfont.woff?v=4.7.0') format('woff'), url('../components/font-awesome/fonts/fontawesome-webfont.ttf?v=4.7.0') format('truetype'), url('../components/font-awesome/fonts/fontawesome-webfont.svg?v=4.7.0#fontawesomeregular') format('svg');
  font-weight: normal;
  font-style: normal;
}
.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
/* makes the font 33% larger relative to the icon container */
.fa-lg {
  font-size: 1.33333333em;
  line-height: 0.75em;
  vertical-align: -15%;
}
.fa-2x {
  font-size: 2em;
}
.fa-3x {
  font-size: 3em;
}
.fa-4x {
  font-size: 4em;
}
.fa-5x {
  font-size: 5em;
}
.fa-fw {
  width: 1.28571429em;
  text-align: center;
}
.fa-ul {
  padding-left: 0;
  margin-left: 2.14285714em;
  list-style-type: none;
}
.fa-ul > li {
  position: relative;
}
.fa-li {
  position: absolute;
  left: -2.14285714em;
  width: 2.14285714em;
  top: 0.14285714em;
  text-align: center;
}
.fa-li.fa-lg {
  left: -1.85714286em;
}
.fa-border {
  padding: .2em .25em .15em;
  border: solid 0.08em #eee;
  border-radius: .1em;
}
.fa-pull-left {
  float: left;
}
.fa-pull-right {
  float: right;
}
.fa.fa-pull-left {
  margin-right: .3em;
}
.fa.fa-pull-right {
  margin-left: .3em;
}
/* Deprecated as of 4.4.0 */
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
.fa.pull-left {
  margin-right: .3em;
}
.fa.pull-right {
  margin-left: .3em;
}
.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
  animation: fa-spin 2s infinite linear;
}
.fa-pulse {
  -webkit-animation: fa-spin 1s infinite steps(8);
  animation: fa-spin 1s infinite steps(8);
}
@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
.fa-rotate-90 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=1)";
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}
.fa-rotate-180 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2)";
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transform: rotate(180deg);
}
.fa-rotate-270 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=3)";
  -webkit-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  transform: rotate(270deg);
}
.fa-flip-horizontal {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1)";
  -webkit-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.fa-flip-vertical {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)";
  -webkit-transform: scale(1, -1);
  -ms-transform: scale(1, -1);
  transform: scale(1, -1);
}
:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical {
  filter: none;
}
.fa-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.fa-stack-1x,
.fa-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.fa-stack-1x {
  line-height: inherit;
}
.fa-stack-2x {
  font-size: 2em;
}
.fa-inverse {
  color: #fff;
}
/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
   readers do not read off random characters that represent icons */
.fa-glass:before {
  content: "\f000";
}
.fa-music:before {
  content: "\f001";
}
.fa-search:before {
  content: "\f002";
}
.fa-envelope-o:before {
  content: "\f003";
}
.fa-heart:before {
  content: "\f004";
}
.fa-star:before {
  content: "\f005";
}
.fa-star-o:before {
  content: "\f006";
}
.fa-user:before {
  content: "\f007";
}
.fa-film:before {
  content: "\f008";
}
.fa-th-large:before {
  content: "\f009";
}
.fa-th:before {
  content: "\f00a";
}
.fa-th-list:before {
  content: "\f00b";
}
.fa-check:before {
  content: "\f00c";
}
.fa-remove:before,
.fa-close:before,
.fa-times:before {
  content: "\f00d";
}
.fa-search-plus:before {
  content: "\f00e";
}
.fa-search-minus:before {
  content: "\f010";
}
.fa-power-off:before {
  content: "\f011";
}
.fa-signal:before {
  content: "\f012";
}
.fa-gear:before,
.fa-cog:before {
  content: "\f013";
}
.fa-trash-o:before {
  content: "\f014";
}
.fa-home:before {
  content: "\f015";
}
.fa-file-o:before {
  content: "\f016";
}
.fa-clock-o:before {
  content: "\f017";
}
.fa-road:before {
  content: "\f018";
}
.fa-download:before {
  content: "\f019";
}
.fa-arrow-circle-o-down:before {
  content: "\f01a";
}
.fa-arrow-circle-o-up:before {
  content: "\f01b";
}
.fa-inbox:before {
  content: "\f01c";
}
.fa-play-circle-o:before {
  content: "\f01d";
}
.fa-rotate-right:before,
.fa-repeat:before {
  content: "\f01e";
}
.fa-refresh:before {
  content: "\f021";
}
.fa-list-alt:before {
  content: "\f022";
}
.fa-lock:before {
  content: "\f023";
}
.fa-flag:before {
  content: "\f024";
}
.fa-headphones:before {
  content: "\f025";
}
.fa-volume-off:before {
  content: "\f026";
}
.fa-volume-down:before {
  content: "\f027";
}
.fa-volume-up:before {
  content: "\f028";
}
.fa-qrcode:before {
  content: "\f029";
}
.fa-barcode:before {
  content: "\f02a";
}
.fa-tag:before {
  content: "\f02b";
}
.fa-tags:before {
  content: "\f02c";
}
.fa-book:before {
  content: "\f02d";
}
.fa-bookmark:before {
  content: "\f02e";
}
.fa-print:before {
  content: "\f02f";
}
.fa-camera:before {
  content: "\f030";
}
.fa-font:before {
  content: "\f031";
}
.fa-bold:before {
  content: "\f032";
}
.fa-italic:before {
  content: "\f033";
}
.fa-text-height:before {
  content: "\f034";
}
.fa-text-width:before {
  content: "\f035";
}
.fa-align-left:before {
  content: "\f036";
}
.fa-align-center:before {
  content: "\f037";
}
.fa-align-right:before {
  content: "\f038";
}
.fa-align-justify:before {
  content: "\f039";
}
.fa-list:before {
  content: "\f03a";
}
.fa-dedent:before,
.fa-outdent:before {
  content: "\f03b";
}
.fa-indent:before {
  content: "\f03c";
}
.fa-video-camera:before {
  content: "\f03d";
}
.fa-photo:before,
.fa-image:before,
.fa-picture-o:before {
  content: "\f03e";
}
.fa-pencil:before {
  content: "\f040";
}
.fa-map-marker:before {
  content: "\f041";
}
.fa-adjust:before {
  content: "\f042";
}
.fa-tint:before {
  content: "\f043";
}
.fa-edit:before,
.fa-pencil-square-o:before {
  content: "\f044";
}
.fa-share-square-o:before {
  content: "\f045";
}
.fa-check-square-o:before {
  content: "\f046";
}
.fa-arrows:before {
  content: "\f047";
}
.fa-step-backward:before {
  content: "\f048";
}
.fa-fast-backward:before {
  content: "\f049";
}
.fa-backward:before {
  content: "\f04a";
}
.fa-play:before {
  content: "\f04b";
}
.fa-pause:before {
  content: "\f04c";
}
.fa-stop:before {
  content: "\f04d";
}
.fa-forward:before {
  content: "\f04e";
}
.fa-fast-forward:before {
  content: "\f050";
}
.fa-step-forward:before {
  content: "\f051";
}
.fa-eject:before {
  content: "\f052";
}
.fa-chevron-left:before {
  content: "\f053";
}
.fa-chevron-right:before {
  content: "\f054";
}
.fa-plus-circle:before {
  content: "\f055";
}
.fa-minus-circle:before {
  content: "\f056";
}
.fa-times-circle:before {
  content: "\f057";
}
.fa-check-circle:before {
  content: "\f058";
}
.fa-question-circle:before {
  content: "\f059";
}
.fa-info-circle:before {
  content: "\f05a";
}
.fa-crosshairs:before {
  content: "\f05b";
}
.fa-times-circle-o:before {
  content: "\f05c";
}
.fa-check-circle-o:before {
  content: "\f05d";
}
.fa-ban:before {
  content: "\f05e";
}
.fa-arrow-left:before {
  content: "\f060";
}
.fa-arrow-right:before {
  content: "\f061";
}
.fa-arrow-up:before {
  content: "\f062";
}
.fa-arrow-down:before {
  content: "\f063";
}
.fa-mail-forward:before,
.fa-share:before {
  content: "\f064";
}
.fa-expand:before {
  content: "\f065";
}
.fa-compress:before {
  content: "\f066";
}
.fa-plus:before {
  content: "\f067";
}
.fa-minus:before {
  content: "\f068";
}
.fa-asterisk:before {
  content: "\f069";
}
.fa-exclamation-circle:before {
  content: "\f06a";
}
.fa-gift:before {
  content: "\f06b";
}
.fa-leaf:before {
  content: "\f06c";
}
.fa-fire:before {
  content: "\f06d";
}
.fa-eye:before {
  content: "\f06e";
}
.fa-eye-slash:before {
  content: "\f070";
}
.fa-warning:before,
.fa-exclamation-triangle:before {
  content: "\f071";
}
.fa-plane:before {
  content: "\f072";
}
.fa-calendar:before {
  content: "\f073";
}
.fa-random:before {
  content: "\f074";
}
.fa-comment:before {
  content: "\f075";
}
.fa-magnet:before {
  content: "\f076";
}
.fa-chevron-up:before {
  content: "\f077";
}
.fa-chevron-down:before {
  content: "\f078";
}
.fa-retweet:before {
  content: "\f079";
}
.fa-shopping-cart:before {
  content: "\f07a";
}
.fa-folder:before {
  content: "\f07b";
}
.fa-folder-open:before {
  content: "\f07c";
}
.fa-arrows-v:before {
  content: "\f07d";
}
.fa-arrows-h:before {
  content: "\f07e";
}
.fa-bar-chart-o:before,
.fa-bar-chart:before {
  content: "\f080";
}
.fa-twitter-square:before {
  content: "\f081";
}
.fa-facebook-square:before {
  content: "\f082";
}
.fa-camera-retro:before {
  content: "\f083";
}
.fa-key:before {
  content: "\f084";
}
.fa-gears:before,
.fa-cogs:before {
  content: "\f085";
}
.fa-comments:before {
  content: "\f086";
}
.fa-thumbs-o-up:before {
  content: "\f087";
}
.fa-thumbs-o-down:before {
  content: "\f088";
}
.fa-star-half:before {
  content: "\f089";
}
.fa-heart-o:before {
  content: "\f08a";
}
.fa-sign-out:before {
  content: "\f08b";
}
.fa-linkedin-square:before {
  content: "\f08c";
}
.fa-thumb-tack:before {
  content: "\f08d";
}
.fa-external-link:before {
  content: "\f08e";
}
.fa-sign-in:before {
  content: "\f090";
}
.fa-trophy:before {
  content: "\f091";
}
.fa-github-square:before {
  content: "\f092";
}
.fa-upload:before {
  content: "\f093";
}
.fa-lemon-o:before {
  content: "\f094";
}
.fa-phone:before {
  content: "\f095";
}
.fa-square-o:before {
  content: "\f096";
}
.fa-bookmark-o:before {
  content: "\f097";
}
.fa-phone-square:before {
  content: "\f098";
}
.fa-twitter:before {
  content: "\f099";
}
.fa-facebook-f:before,
.fa-facebook:before {
  content: "\f09a";
}
.fa-github:before {
  content: "\f09b";
}
.fa-unlock:before {
  content: "\f09c";
}
.fa-credit-card:before {
  content: "\f09d";
}
.fa-feed:before,
.fa-rss:before {
  content: "\f09e";
}
.fa-hdd-o:before {
  content: "\f0a0";
}
.fa-bullhorn:before {
  content: "\f0a1";
}
.fa-bell:before {
  content: "\f0f3";
}
.fa-certificate:before {
  content: "\f0a3";
}
.fa-hand-o-right:before {
  content: "\f0a4";
}
.fa-hand-o-left:before {
  content: "\f0a5";
}
.fa-hand-o-up:before {
  content: "\f0a6";
}
.fa-hand-o-down:before {
  content: "\f0a7";
}
.fa-arrow-circle-left:before {
  content: "\f0a8";
}
.fa-arrow-circle-right:before {
  content: "\f0a9";
}
.fa-arrow-circle-up:before {
  content: "\f0aa";
}
.fa-arrow-circle-down:before {
  content: "\f0ab";
}
.fa-globe:before {
  content: "\f0ac";
}
.fa-wrench:before {
  content: "\f0ad";
}
.fa-tasks:before {
  content: "\f0ae";
}
.fa-filter:before {
  content: "\f0b0";
}
.fa-briefcase:before {
  content: "\f0b1";
}
.fa-arrows-alt:before {
  content: "\f0b2";
}
.fa-group:before,
.fa-users:before {
  content: "\f0c0";
}
.fa-chain:before,
.fa-link:before {
  content: "\f0c1";
}
.fa-cloud:before {
  content: "\f0c2";
}
.fa-flask:before {
  content: "\f0c3";
}
.fa-cut:before,
.fa-scissors:before {
  content: "\f0c4";
}
.fa-copy:before,
.fa-files-o:before {
  content: "\f0c5";
}
.fa-paperclip:before {
  content: "\f0c6";
}
.fa-save:before,
.fa-floppy-o:before {
  content: "\f0c7";
}
.fa-square:before {
  content: "\f0c8";
}
.fa-navicon:before,
.fa-reorder:before,
.fa-bars:before {
  content: "\f0c9";
}
.fa-list-ul:before {
  content: "\f0ca";
}
.fa-list-ol:before {
  content: "\f0cb";
}
.fa-strikethrough:before {
  content: "\f0cc";
}
.fa-underline:before {
  content: "\f0cd";
}
.fa-table:before {
  content: "\f0ce";
}
.fa-magic:before {
  content: "\f0d0";
}
.fa-truck:before {
  content: "\f0d1";
}
.fa-pinterest:before {
  content: "\f0d2";
}
.fa-pinterest-square:before {
  content: "\f0d3";
}
.fa-google-plus-square:before {
  content: "\f0d4";
}
.fa-google-plus:before {
  content: "\f0d5";
}
.fa-money:before {
  content: "\f0d6";
}
.fa-caret-down:before {
  content: "\f0d7";
}
.fa-caret-up:before {
  content: "\f0d8";
}
.fa-caret-left:before {
  content: "\f0d9";
}
.fa-caret-right:before {
  content: "\f0da";
}
.fa-columns:before {
  content: "\f0db";
}
.fa-unsorted:before,
.fa-sort:before {
  content: "\f0dc";
}
.fa-sort-down:before,
.fa-sort-desc:before {
  content: "\f0dd";
}
.fa-sort-up:before,
.fa-sort-asc:before {
  content: "\f0de";
}
.fa-envelope:before {
  content: "\f0e0";
}
.fa-linkedin:before {
  content: "\f0e1";
}
.fa-rotate-left:before,
.fa-undo:before {
  content: "\f0e2";
}
.fa-legal:before,
.fa-gavel:before {
  content: "\f0e3";
}
.fa-dashboard:before,
.fa-tachometer:before {
  content: "\f0e4";
}
.fa-comment-o:before {
  content: "\f0e5";
}
.fa-comments-o:before {
  content: "\f0e6";
}
.fa-flash:before,
.fa-bolt:before {
  content: "\f0e7";
}
.fa-sitemap:before {
  content: "\f0e8";
}
.fa-umbrella:before {
  content: "\f0e9";
}
.fa-paste:before,
.fa-clipboard:before {
  content: "\f0ea";
}
.fa-lightbulb-o:before {
  content: "\f0eb";
}
.fa-exchange:before {
  content: "\f0ec";
}
.fa-cloud-download:before {
  content: "\f0ed";
}
.fa-cloud-upload:before {
  content: "\f0ee";
}
.fa-user-md:before {
  content: "\f0f0";
}
.fa-stethoscope:before {
  content: "\f0f1";
}
.fa-suitcase:before {
  content: "\f0f2";
}
.fa-bell-o:before {
  content: "\f0a2";
}
.fa-coffee:before {
  content: "\f0f4";
}
.fa-cutlery:before {
  content: "\f0f5";
}
.fa-file-text-o:before {
  content: "\f0f6";
}
.fa-building-o:before {
  content: "\f0f7";
}
.fa-hospital-o:before {
  content: "\f0f8";
}
.fa-ambulance:before {
  content: "\f0f9";
}
.fa-medkit:before {
  content: "\f0fa";
}
.fa-fighter-jet:before {
  content: "\f0fb";
}
.fa-beer:before {
  content: "\f0fc";
}
.fa-h-square:before {
  content: "\f0fd";
}
.fa-plus-square:before {
  content: "\f0fe";
}
.fa-angle-double-left:before {
  content: "\f100";
}
.fa-angle-double-right:before {
  content: "\f101";
}
.fa-angle-double-up:before {
  content: "\f102";
}
.fa-angle-double-down:before {
  content: "\f103";
}
.fa-angle-left:before {
  content: "\f104";
}
.fa-angle-right:before {
  content: "\f105";
}
.fa-angle-up:before {
  content: "\f106";
}
.fa-angle-down:before {
  content: "\f107";
}
.fa-desktop:before {
  content: "\f108";
}
.fa-laptop:before {
  content: "\f109";
}
.fa-tablet:before {
  content: "\f10a";
}
.fa-mobile-phone:before,
.fa-mobile:before {
  content: "\f10b";
}
.fa-circle-o:before {
  content: "\f10c";
}
.fa-quote-left:before {
  content: "\f10d";
}
.fa-quote-right:before {
  content: "\f10e";
}
.fa-spinner:before {
  content: "\f110";
}
.fa-circle:before {
  content: "\f111";
}
.fa-mail-reply:before,
.fa-reply:before {
  content: "\f112";
}
.fa-github-alt:before {
  content: "\f113";
}
.fa-folder-o:before {
  content: "\f114";
}
.fa-folder-open-o:before {
  content: "\f115";
}
.fa-smile-o:before {
  content: "\f118";
}
.fa-frown-o:before {
  content: "\f119";
}
.fa-meh-o:before {
  content: "\f11a";
}
.fa-gamepad:before {
  content: "\f11b";
}
.fa-keyboard-o:before {
  content: "\f11c";
}
.fa-flag-o:before {
  content: "\f11d";
}
.fa-flag-checkered:before {
  content: "\f11e";
}
.fa-terminal:before {
  content: "\f120";
}
.fa-code:before {
  content: "\f121";
}
.fa-mail-reply-all:before,
.fa-reply-all:before {
  content: "\f122";
}
.fa-star-half-empty:before,
.fa-star-half-full:before,
.fa-star-half-o:before {
  content: "\f123";
}
.fa-location-arrow:before {
  content: "\f124";
}
.fa-crop:before {
  content: "\f125";
}
.fa-code-fork:before {
  content: "\f126";
}
.fa-unlink:before,
.fa-chain-broken:before {
  content: "\f127";
}
.fa-question:before {
  content: "\f128";
}
.fa-info:before {
  content: "\f129";
}
.fa-exclamation:before {
  content: "\f12a";
}
.fa-superscript:before {
  content: "\f12b";
}
.fa-subscript:before {
  content: "\f12c";
}
.fa-eraser:before {
  content: "\f12d";
}
.fa-puzzle-piece:before {
  content: "\f12e";
}
.fa-microphone:before {
  content: "\f130";
}
.fa-microphone-slash:before {
  content: "\f131";
}
.fa-shield:before {
  content: "\f132";
}
.fa-calendar-o:before {
  content: "\f133";
}
.fa-fire-extinguisher:before {
  content: "\f134";
}
.fa-rocket:before {
  content: "\f135";
}
.fa-maxcdn:before {
  content: "\f136";
}
.fa-chevron-circle-left:before {
  content: "\f137";
}
.fa-chevron-circle-right:before {
  content: "\f138";
}
.fa-chevron-circle-up:before {
  content: "\f139";
}
.fa-chevron-circle-down:before {
  content: "\f13a";
}
.fa-html5:before {
  content: "\f13b";
}
.fa-css3:before {
  content: "\f13c";
}
.fa-anchor:before {
  content: "\f13d";
}
.fa-unlock-alt:before {
  content: "\f13e";
}
.fa-bullseye:before {
  content: "\f140";
}
.fa-ellipsis-h:before {
  content: "\f141";
}
.fa-ellipsis-v:before {
  content: "\f142";
}
.fa-rss-square:before {
  content: "\f143";
}
.fa-play-circle:before {
  content: "\f144";
}
.fa-ticket:before {
  content: "\f145";
}
.fa-minus-square:before {
  content: "\f146";
}
.fa-minus-square-o:before {
  content: "\f147";
}
.fa-level-up:before {
  content: "\f148";
}
.fa-level-down:before {
  content: "\f149";
}
.fa-check-square:before {
  content: "\f14a";
}
.fa-pencil-square:before {
  content: "\f14b";
}
.fa-external-link-square:before {
  content: "\f14c";
}
.fa-share-square:before {
  content: "\f14d";
}
.fa-compass:before {
  content: "\f14e";
}
.fa-toggle-down:before,
.fa-caret-square-o-down:before {
  content: "\f150";
}
.fa-toggle-up:before,
.fa-caret-square-o-up:before {
  content: "\f151";
}
.fa-toggle-right:before,
.fa-caret-square-o-right:before {
  content: "\f152";
}
.fa-euro:before,
.fa-eur:before {
  content: "\f153";
}
.fa-gbp:before {
  content: "\f154";
}
.fa-dollar:before,
.fa-usd:before {
  content: "\f155";
}
.fa-rupee:before,
.fa-inr:before {
  content: "\f156";
}
.fa-cny:before,
.fa-rmb:before,
.fa-yen:before,
.fa-jpy:before {
  content: "\f157";
}
.fa-ruble:before,
.fa-rouble:before,
.fa-rub:before {
  content: "\f158";
}
.fa-won:before,
.fa-krw:before {
  content: "\f159";
}
.fa-bitcoin:before,
.fa-btc:before {
  content: "\f15a";
}
.fa-file:before {
  content: "\f15b";
}
.fa-file-text:before {
  content: "\f15c";
}
.fa-sort-alpha-asc:before {
  content: "\f15d";
}
.fa-sort-alpha-desc:before {
  content: "\f15e";
}
.fa-sort-amount-asc:before {
  content: "\f160";
}
.fa-sort-amount-desc:before {
  content: "\f161";
}
.fa-sort-numeric-asc:before {
  content: "\f162";
}
.fa-sort-numeric-desc:before {
  content: "\f163";
}
.fa-thumbs-up:before {
  content: "\f164";
}
.fa-thumbs-down:before {
  content: "\f165";
}
.fa-youtube-square:before {
  content: "\f166";
}
.fa-youtube:before {
  content: "\f167";
}
.fa-xing:before {
  content: "\f168";
}
.fa-xing-square:before {
  content: "\f169";
}
.fa-youtube-play:before {
  content: "\f16a";
}
.fa-dropbox:before {
  content: "\f16b";
}
.fa-stack-overflow:before {
  content: "\f16c";
}
.fa-instagram:before {
  content: "\f16d";
}
.fa-flickr:before {
  content: "\f16e";
}
.fa-adn:before {
  content: "\f170";
}
.fa-bitbucket:before {
  content: "\f171";
}
.fa-bitbucket-square:before {
  content: "\f172";
}
.fa-tumblr:before {
  content: "\f173";
}
.fa-tumblr-square:before {
  content: "\f174";
}
.fa-long-arrow-down:before {
  content: "\f175";
}
.fa-long-arrow-up:before {
  content: "\f176";
}
.fa-long-arrow-left:before {
  content: "\f177";
}
.fa-long-arrow-right:before {
  content: "\f178";
}
.fa-apple:before {
  content: "\f179";
}
.fa-windows:before {
  content: "\f17a";
}
.fa-android:before {
  content: "\f17b";
}
.fa-linux:before {
  content: "\f17c";
}
.fa-dribbble:before {
  content: "\f17d";
}
.fa-skype:before {
  content: "\f17e";
}
.fa-foursquare:before {
  content: "\f180";
}
.fa-trello:before {
  content: "\f181";
}
.fa-female:before {
  content: "\f182";
}
.fa-male:before {
  content: "\f183";
}
.fa-gittip:before,
.fa-gratipay:before {
  content: "\f184";
}
.fa-sun-o:before {
  content: "\f185";
}
.fa-moon-o:before {
  content: "\f186";
}
.fa-archive:before {
  content: "\f187";
}
.fa-bug:before {
  content: "\f188";
}
.fa-vk:before {
  content: "\f189";
}
.fa-weibo:before {
  content: "\f18a";
}
.fa-renren:before {
  content: "\f18b";
}
.fa-pagelines:before {
  content: "\f18c";
}
.fa-stack-exchange:before {
  content: "\f18d";
}
.fa-arrow-circle-o-right:before {
  content: "\f18e";
}
.fa-arrow-circle-o-left:before {
  content: "\f190";
}
.fa-toggle-left:before,
.fa-caret-square-o-left:before {
  content: "\f191";
}
.fa-dot-circle-o:before {
  content: "\f192";
}
.fa-wheelchair:before {
  content: "\f193";
}
.fa-vimeo-square:before {
  content: "\f194";
}
.fa-turkish-lira:before,
.fa-try:before {
  content: "\f195";
}
.fa-plus-square-o:before {
  content: "\f196";
}
.fa-space-shuttle:before {
  content: "\f197";
}
.fa-slack:before {
  content: "\f198";
}
.fa-envelope-square:before {
  content: "\f199";
}
.fa-wordpress:before {
  content: "\f19a";
}
.fa-openid:before {
  content: "\f19b";
}
.fa-institution:before,
.fa-bank:before,
.fa-university:before {
  content: "\f19c";
}
.fa-mortar-board:before,
.fa-graduation-cap:before {
  content: "\f19d";
}
.fa-yahoo:before {
  content: "\f19e";
}
.fa-google:before {
  content: "\f1a0";
}
.fa-reddit:before {
  content: "\f1a1";
}
.fa-reddit-square:before {
  content: "\f1a2";
}
.fa-stumbleupon-circle:before {
  content: "\f1a3";
}
.fa-stumbleupon:before {
  content: "\f1a4";
}
.fa-delicious:before {
  content: "\f1a5";
}
.fa-digg:before {
  content: "\f1a6";
}
.fa-pied-piper-pp:before {
  content: "\f1a7";
}
.fa-pied-piper-alt:before {
  content: "\f1a8";
}
.fa-drupal:before {
  content: "\f1a9";
}
.fa-joomla:before {
  content: "\f1aa";
}
.fa-language:before {
  content: "\f1ab";
}
.fa-fax:before {
  content: "\f1ac";
}
.fa-building:before {
  content: "\f1ad";
}
.fa-child:before {
  content: "\f1ae";
}
.fa-paw:before {
  content: "\f1b0";
}
.fa-spoon:before {
  content: "\f1b1";
}
.fa-cube:before {
  content: "\f1b2";
}
.fa-cubes:before {
  content: "\f1b3";
}
.fa-behance:before {
  content: "\f1b4";
}
.fa-behance-square:before {
  content: "\f1b5";
}
.fa-steam:before {
  content: "\f1b6";
}
.fa-steam-square:before {
  content: "\f1b7";
}
.fa-recycle:before {
  content: "\f1b8";
}
.fa-automobile:before,
.fa-car:before {
  content: "\f1b9";
}
.fa-cab:before,
.fa-taxi:before {
  content: "\f1ba";
}
.fa-tree:before {
  content: "\f1bb";
}
.fa-spotify:before {
  content: "\f1bc";
}
.fa-deviantart:before {
  content: "\f1bd";
}
.fa-soundcloud:before {
  content: "\f1be";
}
.fa-database:before {
  content: "\f1c0";
}
.fa-file-pdf-o:before {
  content: "\f1c1";
}
.fa-file-word-o:before {
  content: "\f1c2";
}
.fa-file-excel-o:before {
  content: "\f1c3";
}
.fa-file-powerpoint-o:before {
  content: "\f1c4";
}
.fa-file-photo-o:before,
.fa-file-picture-o:before,
.fa-file-image-o:before {
  content: "\f1c5";
}
.fa-file-zip-o:before,
.fa-file-archive-o:before {
  content: "\f1c6";
}
.fa-file-sound-o:before,
.fa-file-audio-o:before {
  content: "\f1c7";
}
.fa-file-movie-o:before,
.fa-file-video-o:before {
  content: "\f1c8";
}
.fa-file-code-o:before {
  content: "\f1c9";
}
.fa-vine:before {
  content: "\f1ca";
}
.fa-codepen:before {
  content: "\f1cb";
}
.fa-jsfiddle:before {
  content: "\f1cc";
}
.fa-life-bouy:before,
.fa-life-buoy:before,
.fa-life-saver:before,
.fa-support:before,
.fa-life-ring:before {
  content: "\f1cd";
}
.fa-circle-o-notch:before {
  content: "\f1ce";
}
.fa-ra:before,
.fa-resistance:before,
.fa-rebel:before {
  content: "\f1d0";
}
.fa-ge:before,
.fa-empire:before {
  content: "\f1d1";
}
.fa-git-square:before {
  content: "\f1d2";
}
.fa-git:before {
  content: "\f1d3";
}
.fa-y-combinator-square:before,
.fa-yc-square:before,
.fa-hacker-news:before {
  content: "\f1d4";
}
.fa-tencent-weibo:before {
  content: "\f1d5";
}
.fa-qq:before {
  content: "\f1d6";
}
.fa-wechat:before,
.fa-weixin:before {
  content: "\f1d7";
}
.fa-send:before,
.fa-paper-plane:before {
  content: "\f1d8";
}
.fa-send-o:before,
.fa-paper-plane-o:before {
  content: "\f1d9";
}
.fa-history:before {
  content: "\f1da";
}
.fa-circle-thin:before {
  content: "\f1db";
}
.fa-header:before {
  content: "\f1dc";
}
.fa-paragraph:before {
  content: "\f1dd";
}
.fa-sliders:before {
  content: "\f1de";
}
.fa-share-alt:before {
  content: "\f1e0";
}
.fa-share-alt-square:before {
  content: "\f1e1";
}
.fa-bomb:before {
  content: "\f1e2";
}
.fa-soccer-ball-o:before,
.fa-futbol-o:before {
  content: "\f1e3";
}
.fa-tty:before {
  content: "\f1e4";
}
.fa-binoculars:before {
  content: "\f1e5";
}
.fa-plug:before {
  content: "\f1e6";
}
.fa-slideshare:before {
  content: "\f1e7";
}
.fa-twitch:before {
  content: "\f1e8";
}
.fa-yelp:before {
  content: "\f1e9";
}
.fa-newspaper-o:before {
  content: "\f1ea";
}
.fa-wifi:before {
  content: "\f1eb";
}
.fa-calculator:before {
  content: "\f1ec";
}
.fa-paypal:before {
  content: "\f1ed";
}
.fa-google-wallet:before {
  content: "\f1ee";
}
.fa-cc-visa:before {
  content: "\f1f0";
}
.fa-cc-mastercard:before {
  content: "\f1f1";
}
.fa-cc-discover:before {
  content: "\f1f2";
}
.fa-cc-amex:before {
  content: "\f1f3";
}
.fa-cc-paypal:before {
  content: "\f1f4";
}
.fa-cc-stripe:before {
  content: "\f1f5";
}
.fa-bell-slash:before {
  content: "\f1f6";
}
.fa-bell-slash-o:before {
  content: "\f1f7";
}
.fa-trash:before {
  content: "\f1f8";
}
.fa-copyright:before {
  content: "\f1f9";
}
.fa-at:before {
  content: "\f1fa";
}
.fa-eyedropper:before {
  content: "\f1fb";
}
.fa-paint-brush:before {
  content: "\f1fc";
}
.fa-birthday-cake:before {
  content: "\f1fd";
}
.fa-area-chart:before {
  content: "\f1fe";
}
.fa-pie-chart:before {
  content: "\f200";
}
.fa-line-chart:before {
  content: "\f201";
}
.fa-lastfm:before {
  content: "\f202";
}
.fa-lastfm-square:before {
  content: "\f203";
}
.fa-toggle-off:before {
  content: "\f204";
}
.fa-toggle-on:before {
  content: "\f205";
}
.fa-bicycle:before {
  content: "\f206";
}
.fa-bus:before {
  content: "\f207";
}
.fa-ioxhost:before {
  content: "\f208";
}
.fa-angellist:before {
  content: "\f209";
}
.fa-cc:before {
  content: "\f20a";
}
.fa-shekel:before,
.fa-sheqel:before,
.fa-ils:before {
  content: "\f20b";
}
.fa-meanpath:before {
  content: "\f20c";
}
.fa-buysellads:before {
  content: "\f20d";
}
.fa-connectdevelop:before {
  content: "\f20e";
}
.fa-dashcube:before {
  content: "\f210";
}
.fa-forumbee:before {
  content: "\f211";
}
.fa-leanpub:before {
  content: "\f212";
}
.fa-sellsy:before {
  content: "\f213";
}
.fa-shirtsinbulk:before {
  content: "\f214";
}
.fa-simplybuilt:before {
  content: "\f215";
}
.fa-skyatlas:before {
  content: "\f216";
}
.fa-cart-plus:before {
  content: "\f217";
}
.fa-cart-arrow-down:before {
  content: "\f218";
}
.fa-diamond:before {
  content: "\f219";
}
.fa-ship:before {
  content: "\f21a";
}
.fa-user-secret:before {
  content: "\f21b";
}
.fa-motorcycle:before {
  content: "\f21c";
}
.fa-street-view:before {
  content: "\f21d";
}
.fa-heartbeat:before {
  content: "\f21e";
}
.fa-venus:before {
  content: "\f221";
}
.fa-mars:before {
  content: "\f222";
}
.fa-mercury:before {
  content: "\f223";
}
.fa-intersex:before,
.fa-transgender:before {
  content: "\f224";
}
.fa-transgender-alt:before {
  content: "\f225";
}
.fa-venus-double:before {
  content: "\f226";
}
.fa-mars-double:before {
  content: "\f227";
}
.fa-venus-mars:before {
  content: "\f228";
}
.fa-mars-stroke:before {
  content: "\f229";
}
.fa-mars-stroke-v:before {
  content: "\f22a";
}
.fa-mars-stroke-h:before {
  content: "\f22b";
}
.fa-neuter:before {
  content: "\f22c";
}
.fa-genderless:before {
  content: "\f22d";
}
.fa-facebook-official:before {
  content: "\f230";
}
.fa-pinterest-p:before {
  content: "\f231";
}
.fa-whatsapp:before {
  content: "\f232";
}
.fa-server:before {
  content: "\f233";
}
.fa-user-plus:before {
  content: "\f234";
}
.fa-user-times:before {
  content: "\f235";
}
.fa-hotel:before,
.fa-bed:before {
  content: "\f236";
}
.fa-viacoin:before {
  content: "\f237";
}
.fa-train:before {
  content: "\f238";
}
.fa-subway:before {
  content: "\f239";
}
.fa-medium:before {
  content: "\f23a";
}
.fa-yc:before,
.fa-y-combinator:before {
  content: "\f23b";
}
.fa-optin-monster:before {
  content: "\f23c";
}
.fa-opencart:before {
  content: "\f23d";
}
.fa-expeditedssl:before {
  content: "\f23e";
}
.fa-battery-4:before,
.fa-battery:before,
.fa-battery-full:before {
  content: "\f240";
}
.fa-battery-3:before,
.fa-battery-three-quarters:before {
  content: "\f241";
}
.fa-battery-2:before,
.fa-battery-half:before {
  content: "\f242";
}
.fa-battery-1:before,
.fa-battery-quarter:before {
  content: "\f243";
}
.fa-battery-0:before,
.fa-battery-empty:before {
  content: "\f244";
}
.fa-mouse-pointer:before {
  content: "\f245";
}
.fa-i-cursor:before {
  content: "\f246";
}
.fa-object-group:before {
  content: "\f247";
}
.fa-object-ungroup:before {
  content: "\f248";
}
.fa-sticky-note:before {
  content: "\f249";
}
.fa-sticky-note-o:before {
  content: "\f24a";
}
.fa-cc-jcb:before {
  content: "\f24b";
}
.fa-cc-diners-club:before {
  content: "\f24c";
}
.fa-clone:before {
  content: "\f24d";
}
.fa-balance-scale:before {
  content: "\f24e";
}
.fa-hourglass-o:before {
  content: "\f250";
}
.fa-hourglass-1:before,
.fa-hourglass-start:before {
  content: "\f251";
}
.fa-hourglass-2:before,
.fa-hourglass-half:before {
  content: "\f252";
}
.fa-hourglass-3:before,
.fa-hourglass-end:before {
  content: "\f253";
}
.fa-hourglass:before {
  content: "\f254";
}
.fa-hand-grab-o:before,
.fa-hand-rock-o:before {
  content: "\f255";
}
.fa-hand-stop-o:before,
.fa-hand-paper-o:before {
  content: "\f256";
}
.fa-hand-scissors-o:before {
  content: "\f257";
}
.fa-hand-lizard-o:before {
  content: "\f258";
}
.fa-hand-spock-o:before {
  content: "\f259";
}
.fa-hand-pointer-o:before {
  content: "\f25a";
}
.fa-hand-peace-o:before {
  content: "\f25b";
}
.fa-trademark:before {
  content: "\f25c";
}
.fa-registered:before {
  content: "\f25d";
}
.fa-creative-commons:before {
  content: "\f25e";
}
.fa-gg:before {
  content: "\f260";
}
.fa-gg-circle:before {
  content: "\f261";
}
.fa-tripadvisor:before {
  content: "\f262";
}
.fa-odnoklassniki:before {
  content: "\f263";
}
.fa-odnoklassniki-square:before {
  content: "\f264";
}
.fa-get-pocket:before {
  content: "\f265";
}
.fa-wikipedia-w:before {
  content: "\f266";
}
.fa-safari:before {
  content: "\f267";
}
.fa-chrome:before {
  content: "\f268";
}
.fa-firefox:before {
  content: "\f269";
}
.fa-opera:before {
  content: "\f26a";
}
.fa-internet-explorer:before {
  content: "\f26b";
}
.fa-tv:before,
.fa-television:before {
  content: "\f26c";
}
.fa-contao:before {
  content: "\f26d";
}
.fa-500px:before {
  content: "\f26e";
}
.fa-amazon:before {
  content: "\f270";
}
.fa-calendar-plus-o:before {
  content: "\f271";
}
.fa-calendar-minus-o:before {
  content: "\f272";
}
.fa-calendar-times-o:before {
  content: "\f273";
}
.fa-calendar-check-o:before {
  content: "\f274";
}
.fa-industry:before {
  content: "\f275";
}
.fa-map-pin:before {
  content: "\f276";
}
.fa-map-signs:before {
  content: "\f277";
}
.fa-map-o:before {
  content: "\f278";
}
.fa-map:before {
  content: "\f279";
}
.fa-commenting:before {
  content: "\f27a";
}
.fa-commenting-o:before {
  content: "\f27b";
}
.fa-houzz:before {
  content: "\f27c";
}
.fa-vimeo:before {
  content: "\f27d";
}
.fa-black-tie:before {
  content: "\f27e";
}
.fa-fonticons:before {
  content: "\f280";
}
.fa-reddit-alien:before {
  content: "\f281";
}
.fa-edge:before {
  content: "\f282";
}
.fa-credit-card-alt:before {
  content: "\f283";
}
.fa-codiepie:before {
  content: "\f284";
}
.fa-modx:before {
  content: "\f285";
}
.fa-fort-awesome:before {
  content: "\f286";
}
.fa-usb:before {
  content: "\f287";
}
.fa-product-hunt:before {
  content: "\f288";
}
.fa-mixcloud:before {
  content: "\f289";
}
.fa-scribd:before {
  content: "\f28a";
}
.fa-pause-circle:before {
  content: "\f28b";
}
.fa-pause-circle-o:before {
  content: "\f28c";
}
.fa-stop-circle:before {
  content: "\f28d";
}
.fa-stop-circle-o:before {
  content: "\f28e";
}
.fa-shopping-bag:before {
  content: "\f290";
}
.fa-shopping-basket:before {
  content: "\f291";
}
.fa-hashtag:before {
  content: "\f292";
}
.fa-bluetooth:before {
  content: "\f293";
}
.fa-bluetooth-b:before {
  content: "\f294";
}
.fa-percent:before {
  content: "\f295";
}
.fa-gitlab:before {
  content: "\f296";
}
.fa-wpbeginner:before {
  content: "\f297";
}
.fa-wpforms:before {
  content: "\f298";
}
.fa-envira:before {
  content: "\f299";
}
.fa-universal-access:before {
  content: "\f29a";
}
.fa-wheelchair-alt:before {
  content: "\f29b";
}
.fa-question-circle-o:before {
  content: "\f29c";
}
.fa-blind:before {
  content: "\f29d";
}
.fa-audio-description:before {
  content: "\f29e";
}
.fa-volume-control-phone:before {
  content: "\f2a0";
}
.fa-braille:before {
  content: "\f2a1";
}
.fa-assistive-listening-systems:before {
  content: "\f2a2";
}
.fa-asl-interpreting:before,
.fa-american-sign-language-interpreting:before {
  content: "\f2a3";
}
.fa-deafness:before,
.fa-hard-of-hearing:before,
.fa-deaf:before {
  content: "\f2a4";
}
.fa-glide:before {
  content: "\f2a5";
}
.fa-glide-g:before {
  content: "\f2a6";
}
.fa-signing:before,
.fa-sign-language:before {
  content: "\f2a7";
}
.fa-low-vision:before {
  content: "\f2a8";
}
.fa-viadeo:before {
  content: "\f2a9";
}
.fa-viadeo-square:before {
  content: "\f2aa";
}
.fa-snapchat:before {
  content: "\f2ab";
}
.fa-snapchat-ghost:before {
  content: "\f2ac";
}
.fa-snapchat-square:before {
  content: "\f2ad";
}
.fa-pied-piper:before {
  content: "\f2ae";
}
.fa-first-order:before {
  content: "\f2b0";
}
.fa-yoast:before {
  content: "\f2b1";
}
.fa-themeisle:before {
  content: "\f2b2";
}
.fa-google-plus-circle:before,
.fa-google-plus-official:before {
  content: "\f2b3";
}
.fa-fa:before,
.fa-font-awesome:before {
  content: "\f2b4";
}
.fa-handshake-o:before {
  content: "\f2b5";
}
.fa-envelope-open:before {
  content: "\f2b6";
}
.fa-envelope-open-o:before {
  content: "\f2b7";
}
.fa-linode:before {
  content: "\f2b8";
}
.fa-address-book:before {
  content: "\f2b9";
}
.fa-address-book-o:before {
  content: "\f2ba";
}
.fa-vcard:before,
.fa-address-card:before {
  content: "\f2bb";
}
.fa-vcard-o:before,
.fa-address-card-o:before {
  content: "\f2bc";
}
.fa-user-circle:before {
  content: "\f2bd";
}
.fa-user-circle-o:before {
  content: "\f2be";
}
.fa-user-o:before {
  content: "\f2c0";
}
.fa-id-badge:before {
  content: "\f2c1";
}
.fa-drivers-license:before,
.fa-id-card:before {
  content: "\f2c2";
}
.fa-drivers-license-o:before,
.fa-id-card-o:before {
  content: "\f2c3";
}
.fa-quora:before {
  content: "\f2c4";
}
.fa-free-code-camp:before {
  content: "\f2c5";
}
.fa-telegram:before {
  content: "\f2c6";
}
.fa-thermometer-4:before,
.fa-thermometer:before,
.fa-thermometer-full:before {
  content: "\f2c7";
}
.fa-thermometer-3:before,
.fa-thermometer-three-quarters:before {
  content: "\f2c8";
}
.fa-thermometer-2:before,
.fa-thermometer-half:before {
  content: "\f2c9";
}
.fa-thermometer-1:before,
.fa-thermometer-quarter:before {
  content: "\f2ca";
}
.fa-thermometer-0:before,
.fa-thermometer-empty:before {
  content: "\f2cb";
}
.fa-shower:before {
  content: "\f2cc";
}
.fa-bathtub:before,
.fa-s15:before,
.fa-bath:before {
  content: "\f2cd";
}
.fa-podcast:before {
  content: "\f2ce";
}
.fa-window-maximize:before {
  content: "\f2d0";
}
.fa-window-minimize:before {
  content: "\f2d1";
}
.fa-window-restore:before {
  content: "\f2d2";
}
.fa-times-rectangle:before,
.fa-window-close:before {
  content: "\f2d3";
}
.fa-times-rectangle-o:before,
.fa-window-close-o:before {
  content: "\f2d4";
}
.fa-bandcamp:before {
  content: "\f2d5";
}
.fa-grav:before {
  content: "\f2d6";
}
.fa-etsy:before {
  content: "\f2d7";
}
.fa-imdb:before {
  content: "\f2d8";
}
.fa-ravelry:before {
  content: "\f2d9";
}
.fa-eercast:before {
  content: "\f2da";
}
.fa-microchip:before {
  content: "\f2db";
}
.fa-snowflake-o:before {
  content: "\f2dc";
}
.fa-superpowers:before {
  content: "\f2dd";
}
.fa-wpexplorer:before {
  content: "\f2de";
}
.fa-meetup:before {
  content: "\f2e0";
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
/*!
*
* IPython base
*
*/
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
code {
  color: #000;
}
pre {
  font-size: inherit;
  line-height: inherit;
}
label {
  font-weight: normal;
}
/* Make the page background atleast 100% the height of the view port */
/* Make the page itself atleast 70% the height of the view port */
.border-box-sizing {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.corner-all {
  border-radius: 2px;
}
.no-padding {
  padding: 0px;
}
/* Flexible box model classes */
/* Taken from Alex Russell http://infrequently.org/2009/08/css-3-progress/ */
/* This file is a compatability layer.  It allows the usage of flexible box 
model layouts accross multiple browsers, including older browsers.  The newest,
universal implementation of the flexible box model is used when available (see
`Modern browsers` comments below).  Browsers that are known to implement this 
new spec completely include:

    Firefox 28.0+
    Chrome 29.0+
    Internet Explorer 11+ 
    Opera 17.0+

Browsers not listed, including Safari, are supported via the styling under the
`Old browsers` comments below.
*/
.hbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
.hbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.vbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.vbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.hbox.reverse,
.vbox.reverse,
.reverse {
  /* Old browsers */
  -webkit-box-direction: reverse;
  -moz-box-direction: reverse;
  box-direction: reverse;
  /* Modern browsers */
  flex-direction: row-reverse;
}
.hbox.box-flex0,
.vbox.box-flex0,
.box-flex0 {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  width: auto;
}
.hbox.box-flex1,
.vbox.box-flex1,
.box-flex1 {
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex,
.vbox.box-flex,
.box-flex {
  /* Old browsers */
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex2,
.vbox.box-flex2,
.box-flex2 {
  /* Old browsers */
  -webkit-box-flex: 2;
  -moz-box-flex: 2;
  box-flex: 2;
  /* Modern browsers */
  flex: 2;
}
.box-group1 {
  /*  Deprecated */
  -webkit-box-flex-group: 1;
  -moz-box-flex-group: 1;
  box-flex-group: 1;
}
.box-group2 {
  /* Deprecated */
  -webkit-box-flex-group: 2;
  -moz-box-flex-group: 2;
  box-flex-group: 2;
}
.hbox.start,
.vbox.start,
.start {
  /* Old browsers */
  -webkit-box-pack: start;
  -moz-box-pack: start;
  box-pack: start;
  /* Modern browsers */
  justify-content: flex-start;
}
.hbox.end,
.vbox.end,
.end {
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
}
.hbox.center,
.vbox.center,
.center {
  /* Old browsers */
  -webkit-box-pack: center;
  -moz-box-pack: center;
  box-pack: center;
  /* Modern browsers */
  justify-content: center;
}
.hbox.baseline,
.vbox.baseline,
.baseline {
  /* Old browsers */
  -webkit-box-pack: baseline;
  -moz-box-pack: baseline;
  box-pack: baseline;
  /* Modern browsers */
  justify-content: baseline;
}
.hbox.stretch,
.vbox.stretch,
.stretch {
  /* Old browsers */
  -webkit-box-pack: stretch;
  -moz-box-pack: stretch;
  box-pack: stretch;
  /* Modern browsers */
  justify-content: stretch;
}
.hbox.align-start,
.vbox.align-start,
.align-start {
  /* Old browsers */
  -webkit-box-align: start;
  -moz-box-align: start;
  box-align: start;
  /* Modern browsers */
  align-items: flex-start;
}
.hbox.align-end,
.vbox.align-end,
.align-end {
  /* Old browsers */
  -webkit-box-align: end;
  -moz-box-align: end;
  box-align: end;
  /* Modern browsers */
  align-items: flex-end;
}
.hbox.align-center,
.vbox.align-center,
.align-center {
  /* Old browsers */
  -webkit-box-align: center;
  -moz-box-align: center;
  box-align: center;
  /* Modern browsers */
  align-items: center;
}
.hbox.align-baseline,
.vbox.align-baseline,
.align-baseline {
  /* Old browsers */
  -webkit-box-align: baseline;
  -moz-box-align: baseline;
  box-align: baseline;
  /* Modern browsers */
  align-items: baseline;
}
.hbox.align-stretch,
.vbox.align-stretch,
.align-stretch {
  /* Old browsers */
  -webkit-box-align: stretch;
  -moz-box-align: stretch;
  box-align: stretch;
  /* Modern browsers */
  align-items: stretch;
}
div.error {
  margin: 2em;
  text-align: center;
}
div.error > h1 {
  font-size: 500%;
  line-height: normal;
}
div.error > p {
  font-size: 200%;
  line-height: normal;
}
div.traceback-wrapper {
  text-align: left;
  max-width: 800px;
  margin: auto;
}
div.traceback-wrapper pre.traceback {
  max-height: 600px;
  overflow: auto;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
body {
  background-color: #fff;
  /* This makes sure that the body covers the entire window and needs to
       be in a different element than the display: box in wrapper below */
  position: absolute;
  left: 0px;
  right: 0px;
  top: 0px;
  bottom: 0px;
  overflow: visible;
}
body > #header {
  /* Initially hidden to prevent FLOUC */
  display: none;
  background-color: #fff;
  /* Display over codemirror */
  position: relative;
  z-index: 100;
}
body > #header #header-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 5px;
  padding-bottom: 5px;
  padding-top: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
body > #header .header-bar {
  width: 100%;
  height: 1px;
  background: #e7e7e7;
  margin-bottom: -1px;
}
@media print {
  body > #header {
    display: none !important;
  }
}
#header-spacer {
  width: 100%;
  visibility: hidden;
}
@media print {
  #header-spacer {
    display: none;
  }
}
#ipython_notebook {
  padding-left: 0px;
  padding-top: 1px;
  padding-bottom: 1px;
}
[dir="rtl"] #ipython_notebook {
  margin-right: 10px;
  margin-left: 0;
}
[dir="rtl"] #ipython_notebook.pull-left {
  float: right !important;
  float: right;
}
.flex-spacer {
  flex: 1;
}
#noscript {
  width: auto;
  padding-top: 16px;
  padding-bottom: 16px;
  text-align: center;
  font-size: 22px;
  color: red;
  font-weight: bold;
}
#ipython_notebook img {
  height: 28px;
}
#site {
  width: 100%;
  display: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  overflow: auto;
}
@media print {
  #site {
    height: auto !important;
  }
}
/* Smaller buttons */
.ui-button .ui-button-text {
  padding: 0.2em 0.8em;
  font-size: 77%;
}
input.ui-button {
  padding: 0.3em 0.9em;
}
span#kernel_logo_widget {
  margin: 0 10px;
}
span#login_widget {
  float: right;
}
[dir="rtl"] span#login_widget {
  float: left;
}
span#login_widget > .button,
#logout {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button:focus,
#logout:focus,
span#login_widget > .button.focus,
#logout.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
span#login_widget > .button:hover,
#logout:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active:hover,
#logout:active:hover,
span#login_widget > .button.active:hover,
#logout.active:hover,
.open > .dropdown-togglespan#login_widget > .button:hover,
.open > .dropdown-toggle#logout:hover,
span#login_widget > .button:active:focus,
#logout:active:focus,
span#login_widget > .button.active:focus,
#logout.active:focus,
.open > .dropdown-togglespan#login_widget > .button:focus,
.open > .dropdown-toggle#logout:focus,
span#login_widget > .button:active.focus,
#logout:active.focus,
span#login_widget > .button.active.focus,
#logout.active.focus,
.open > .dropdown-togglespan#login_widget > .button.focus,
.open > .dropdown-toggle#logout.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  background-image: none;
}
span#login_widget > .button.disabled:hover,
#logout.disabled:hover,
span#login_widget > .button[disabled]:hover,
#logout[disabled]:hover,
fieldset[disabled] span#login_widget > .button:hover,
fieldset[disabled] #logout:hover,
span#login_widget > .button.disabled:focus,
#logout.disabled:focus,
span#login_widget > .button[disabled]:focus,
#logout[disabled]:focus,
fieldset[disabled] span#login_widget > .button:focus,
fieldset[disabled] #logout:focus,
span#login_widget > .button.disabled.focus,
#logout.disabled.focus,
span#login_widget > .button[disabled].focus,
#logout[disabled].focus,
fieldset[disabled] span#login_widget > .button.focus,
fieldset[disabled] #logout.focus {
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button .badge,
#logout .badge {
  color: #fff;
  background-color: #333;
}
.nav-header {
  text-transform: none;
}
#header > span {
  margin-top: 10px;
}
.modal_stretch .modal-dialog {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  min-height: 80vh;
}
.modal_stretch .modal-dialog .modal-body {
  max-height: calc(100vh - 200px);
  overflow: auto;
  flex: 1;
}
.modal-header {
  cursor: move;
}
@media (min-width: 768px) {
  .modal .modal-dialog {
    width: 700px;
  }
}
@media (min-width: 768px) {
  select.form-control {
    margin-left: 12px;
    margin-right: 12px;
  }
}
/*!
*
* IPython auth
*
*/
.center-nav {
  display: inline-block;
  margin-bottom: -4px;
}
[dir="rtl"] .center-nav form.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] .center-nav .navbar-text {
  float: right;
}
[dir="rtl"] .navbar-inner {
  text-align: right;
}
[dir="rtl"] div.text-left {
  text-align: right;
}
/*!
*
* IPython tree view
*
*/
/* We need an invisible input field on top of the sentense*/
/* "Drag file onto the list ..." */
.alternate_upload {
  background-color: none;
  display: inline;
}
.alternate_upload.form {
  padding: 0;
  margin: 0;
}
.alternate_upload input.fileinput {
  position: absolute;
  display: block;
  width: 100%;
  height: 100%;
  overflow: hidden;
  cursor: pointer;
  opacity: 0;
  z-index: 2;
}
.alternate_upload .btn-xs > input.fileinput {
  margin: -1px -5px;
}
.alternate_upload .btn-upload {
  position: relative;
  height: 22px;
}
::-webkit-file-upload-button {
  cursor: pointer;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
ul#tabs {
  margin-bottom: 4px;
}
ul#tabs a {
  padding-top: 6px;
  padding-bottom: 4px;
}
[dir="rtl"] ul#tabs.nav-tabs > li {
  float: right;
}
[dir="rtl"] ul#tabs.nav.nav-tabs {
  padding-right: 0;
}
ul.breadcrumb a:focus,
ul.breadcrumb a:hover {
  text-decoration: none;
}
ul.breadcrumb i.icon-home {
  font-size: 16px;
  margin-right: 4px;
}
ul.breadcrumb span {
  color: #5e5e5e;
}
.list_toolbar {
  padding: 4px 0 4px 0;
  vertical-align: middle;
}
.list_toolbar .tree-buttons {
  padding-top: 1px;
}
[dir="rtl"] .list_toolbar .tree-buttons .pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .list_toolbar .col-sm-4,
[dir="rtl"] .list_toolbar .col-sm-8 {
  float: right;
}
.dynamic-buttons {
  padding-top: 3px;
  display: inline-block;
}
.list_toolbar [class*="span"] {
  min-height: 24px;
}
.list_header {
  font-weight: bold;
  background-color: #EEE;
}
.list_placeholder {
  font-weight: bold;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
}
.list_container {
  margin-top: 4px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 2px;
}
.list_container > div {
  border-bottom: 1px solid #ddd;
}
.list_container > div:hover .list-item {
  background-color: red;
}
.list_container > div:last-child {
  border: none;
}
.list_item:hover .list_item {
  background-color: #ddd;
}
.list_item a {
  text-decoration: none;
}
.list_item:hover {
  background-color: #fafafa;
}
.list_header > div,
.list_item > div {
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
.list_header > div input,
.list_item > div input {
  margin-right: 7px;
  margin-left: 14px;
  vertical-align: text-bottom;
  line-height: 22px;
  position: relative;
  top: -1px;
}
.list_header > div .item_link,
.list_item > div .item_link {
  margin-left: -1px;
  vertical-align: baseline;
  line-height: 22px;
}
[dir="rtl"] .list_item > div input {
  margin-right: 0;
}
.new-file input[type=checkbox] {
  visibility: hidden;
}
.item_name {
  line-height: 22px;
  height: 24px;
}
.item_icon {
  font-size: 14px;
  color: #5e5e5e;
  margin-right: 7px;
  margin-left: 7px;
  line-height: 22px;
  vertical-align: baseline;
}
.item_modified {
  margin-right: 7px;
  margin-left: 7px;
}
[dir="rtl"] .item_modified.pull-right {
  float: left !important;
  float: left;
}
.item_buttons {
  line-height: 1em;
  margin-left: -5px;
}
.item_buttons .btn,
.item_buttons .btn-group,
.item_buttons .input-group {
  float: left;
}
.item_buttons > .btn,
.item_buttons > .btn-group,
.item_buttons > .input-group {
  margin-left: 5px;
}
.item_buttons .btn {
  min-width: 13ex;
}
.item_buttons .running-indicator {
  padding-top: 4px;
  color: #5cb85c;
}
.item_buttons .kernel-name {
  padding-top: 4px;
  color: #5bc0de;
  margin-right: 7px;
  float: left;
}
[dir="rtl"] .item_buttons.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .item_buttons .kernel-name {
  margin-left: 7px;
  float: right;
}
.toolbar_info {
  height: 24px;
  line-height: 24px;
}
.list_item input:not([type=checkbox]) {
  padding-top: 3px;
  padding-bottom: 3px;
  height: 22px;
  line-height: 14px;
  margin: 0px;
}
.highlight_text {
  color: blue;
}
#project_name {
  display: inline-block;
  padding-left: 7px;
  margin-left: -2px;
}
#project_name > .breadcrumb {
  padding: 0px;
  margin-bottom: 0px;
  background-color: transparent;
  font-weight: bold;
}
.sort_button {
  display: inline-block;
  padding-left: 7px;
}
[dir="rtl"] .sort_button.pull-right {
  float: left !important;
  float: left;
}
#tree-selector {
  padding-right: 0px;
}
#button-select-all {
  min-width: 50px;
}
[dir="rtl"] #button-select-all.btn {
  float: right ;
}
#select-all {
  margin-left: 7px;
  margin-right: 2px;
  margin-top: 2px;
  height: 16px;
}
[dir="rtl"] #select-all.pull-left {
  float: right !important;
  float: right;
}
.menu_icon {
  margin-right: 2px;
}
.tab-content .row {
  margin-left: 0px;
  margin-right: 0px;
}
.folder_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f114";
}
.folder_icon:before.fa-pull-left {
  margin-right: .3em;
}
.folder_icon:before.fa-pull-right {
  margin-left: .3em;
}
.folder_icon:before.pull-left {
  margin-right: .3em;
}
.folder_icon:before.pull-right {
  margin-left: .3em;
}
.notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
}
.notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.notebook_icon:before.pull-left {
  margin-right: .3em;
}
.notebook_icon:before.pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
  color: #5cb85c;
}
.running_notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before.pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.pull-right {
  margin-left: .3em;
}
.file_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f016";
  position: relative;
  top: -2px;
}
.file_icon:before.fa-pull-left {
  margin-right: .3em;
}
.file_icon:before.fa-pull-right {
  margin-left: .3em;
}
.file_icon:before.pull-left {
  margin-right: .3em;
}
.file_icon:before.pull-right {
  margin-left: .3em;
}
#notebook_toolbar .pull-right {
  padding-top: 0px;
  margin-right: -1px;
}
ul#new-menu {
  left: auto;
  right: 0;
}
#new-menu .dropdown-header {
  font-size: 10px;
  border-bottom: 1px solid #e5e5e5;
  padding: 0 0 3px;
  margin: -3px 20px 0;
}
.kernel-menu-icon {
  padding-right: 12px;
  width: 24px;
  content: "\f096";
}
.kernel-menu-icon:before {
  content: "\f096";
}
.kernel-menu-icon-current:before {
  content: "\f00c";
}
#tab_content {
  padding-top: 20px;
}
#running .panel-group .panel {
  margin-top: 3px;
  margin-bottom: 1em;
}
#running .panel-group .panel .panel-heading {
  background-color: #EEE;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
#running .panel-group .panel .panel-heading a:focus,
#running .panel-group .panel .panel-heading a:hover {
  text-decoration: none;
}
#running .panel-group .panel .panel-body {
  padding: 0px;
}
#running .panel-group .panel .panel-body .list_container {
  margin-top: 0px;
  margin-bottom: 0px;
  border: 0px;
  border-radius: 0px;
}
#running .panel-group .panel .panel-body .list_container .list_item {
  border-bottom: 1px solid #ddd;
}
#running .panel-group .panel .panel-body .list_container .list_item:last-child {
  border-bottom: 0px;
}
.delete-button {
  display: none;
}
.duplicate-button {
  display: none;
}
.rename-button {
  display: none;
}
.move-button {
  display: none;
}
.download-button {
  display: none;
}
.shutdown-button {
  display: none;
}
.dynamic-instructions {
  display: inline-block;
  padding-top: 4px;
}
/*!
*
* IPython text editor webapp
*
*/
.selected-keymap i.fa {
  padding: 0px 5px;
}
.selected-keymap i.fa:before {
  content: "\f00c";
}
#mode-menu {
  overflow: auto;
  max-height: 20em;
}
.edit_app #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.edit_app #menubar .navbar {
  /* Use a negative 1 bottom margin, so the border overlaps the border of the
    header */
  margin-bottom: -1px;
}
.dirty-indicator {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator.pull-left {
  margin-right: .3em;
}
.dirty-indicator.pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-dirty.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty.pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-clean.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f00c";
}
.dirty-indicator-clean:before.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.pull-right {
  margin-left: .3em;
}
#filename {
  font-size: 16pt;
  display: table;
  padding: 0px 5px;
}
#current-mode {
  padding-left: 5px;
  padding-right: 5px;
}
#texteditor-backdrop {
  padding-top: 20px;
  padding-bottom: 20px;
}
@media not print {
  #texteditor-backdrop {
    background-color: #EEE;
  }
}
@media print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container {
    padding: 0px;
    background-color: #fff;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
.CodeMirror-dialog {
  background-color: #fff;
}
/*!
*
* IPython notebook
*
*/
/* CSS font colors for translated ANSI escape sequences */
/* The color values are a mix of
   http://www.xcolors.net/dl/baskerville-ivorylight and
   http://www.xcolors.net/dl/euphrasia */
.ansi-black-fg {
  color: #3E424D;
}
.ansi-black-bg {
  background-color: #3E424D;
}
.ansi-black-intense-fg {
  color: #282C36;
}
.ansi-black-intense-bg {
  background-color: #282C36;
}
.ansi-red-fg {
  color: #E75C58;
}
.ansi-red-bg {
  background-color: #E75C58;
}
.ansi-red-intense-fg {
  color: #B22B31;
}
.ansi-red-intense-bg {
  background-color: #B22B31;
}
.ansi-green-fg {
  color: #00A250;
}
.ansi-green-bg {
  background-color: #00A250;
}
.ansi-green-intense-fg {
  color: #007427;
}
.ansi-green-intense-bg {
  background-color: #007427;
}
.ansi-yellow-fg {
  color: #DDB62B;
}
.ansi-yellow-bg {
  background-color: #DDB62B;
}
.ansi-yellow-intense-fg {
  color: #B27D12;
}
.ansi-yellow-intense-bg {
  background-color: #B27D12;
}
.ansi-blue-fg {
  color: #208FFB;
}
.ansi-blue-bg {
  background-color: #208FFB;
}
.ansi-blue-intense-fg {
  color: #0065CA;
}
.ansi-blue-intense-bg {
  background-color: #0065CA;
}
.ansi-magenta-fg {
  color: #D160C4;
}
.ansi-magenta-bg {
  background-color: #D160C4;
}
.ansi-magenta-intense-fg {
  color: #A03196;
}
.ansi-magenta-intense-bg {
  background-color: #A03196;
}
.ansi-cyan-fg {
  color: #60C6C8;
}
.ansi-cyan-bg {
  background-color: #60C6C8;
}
.ansi-cyan-intense-fg {
  color: #258F8F;
}
.ansi-cyan-intense-bg {
  background-color: #258F8F;
}
.ansi-white-fg {
  color: #C5C1B4;
}
.ansi-white-bg {
  background-color: #C5C1B4;
}
.ansi-white-intense-fg {
  color: #A1A6B2;
}
.ansi-white-intense-bg {
  background-color: #A1A6B2;
}
.ansi-default-inverse-fg {
  color: #FFFFFF;
}
.ansi-default-inverse-bg {
  background-color: #000000;
}
.ansi-bold {
  font-weight: bold;
}
.ansi-underline {
  text-decoration: underline;
}
/* The following styles are deprecated an will be removed in a future version */
.ansibold {
  font-weight: bold;
}
.ansi-inverse {
  outline: 0.5px dotted;
}
/* use dark versions for foreground, to improve visibility */
.ansiblack {
  color: black;
}
.ansired {
  color: darkred;
}
.ansigreen {
  color: darkgreen;
}
.ansiyellow {
  color: #c4a000;
}
.ansiblue {
  color: darkblue;
}
.ansipurple {
  color: darkviolet;
}
.ansicyan {
  color: steelblue;
}
.ansigray {
  color: gray;
}
/* and light for background, for the same reason */
.ansibgblack {
  background-color: black;
}
.ansibgred {
  background-color: red;
}
.ansibggreen {
  background-color: green;
}
.ansibgyellow {
  background-color: yellow;
}
.ansibgblue {
  background-color: blue;
}
.ansibgpurple {
  background-color: magenta;
}
.ansibgcyan {
  background-color: cyan;
}
.ansibggray {
  background-color: gray;
}
div.cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-radius: 2px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  border-width: 1px;
  border-style: solid;
  border-color: transparent;
  width: 100%;
  padding: 5px;
  /* This acts as a spacer between cells, that is outside the border */
  margin: 0px;
  outline: none;
  position: relative;
  overflow: visible;
}
div.cell:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: transparent;
}
div.cell.jupyter-soft-selected {
  border-left-color: #E3F2FD;
  border-left-width: 1px;
  padding-left: 5px;
  border-right-color: #E3F2FD;
  border-right-width: 1px;
  background: #E3F2FD;
}
@media print {
  div.cell.jupyter-soft-selected {
    border-color: transparent;
  }
}
div.cell.selected,
div.cell.selected.jupyter-soft-selected {
  border-color: #ababab;
}
div.cell.selected:before,
div.cell.selected.jupyter-soft-selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #42A5F5;
}
@media print {
  div.cell.selected,
  div.cell.selected.jupyter-soft-selected {
    border-color: transparent;
  }
}
.edit_mode div.cell.selected {
  border-color: #66BB6A;
}
.edit_mode div.cell.selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #66BB6A;
}
@media print {
  .edit_mode div.cell.selected {
    border-color: transparent;
  }
}
.prompt {
  /* This needs to be wide enough for 3 digit prompt numbers: In[100]: */
  min-width: 14ex;
  /* This padding is tuned to match the padding on the CodeMirror editor. */
  padding: 0.4em;
  margin: 0px;
  font-family: monospace;
  text-align: right;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
  /* Don't highlight prompt number selection */
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  /* Use default cursor */
  cursor: default;
}
@media (max-width: 540px) {
  .prompt {
    text-align: left;
  }
}
div.inner_cell {
  min-width: 0;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_area {
  border: 1px solid #cfcfcf;
  border-radius: 2px;
  background: #f7f7f7;
  line-height: 1.21429em;
}
/* This is needed so that empty prompt areas can collapse to zero height when there
   is no content in the output_subarea and the prompt. The main purpose of this is
   to make sure that empty JavaScript output_subareas have no height. */
div.prompt:empty {
  padding-top: 0;
  padding-bottom: 0;
}
div.unrecognized_cell {
  padding: 5px 5px 5px 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.unrecognized_cell .inner_cell {
  border-radius: 2px;
  padding: 5px;
  font-weight: bold;
  color: red;
  border: 1px solid #cfcfcf;
  background: #eaeaea;
}
div.unrecognized_cell .inner_cell a {
  color: inherit;
  text-decoration: none;
}
div.unrecognized_cell .inner_cell a:hover {
  color: inherit;
  text-decoration: none;
}
@media (max-width: 540px) {
  div.unrecognized_cell > div.prompt {
    display: none;
  }
}
div.code_cell {
  /* avoid page breaking on code cells when printing */
}
@media print {
  div.code_cell {
    page-break-inside: avoid;
  }
}
/* any special styling for code cells that are currently running goes here */
div.input {
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.input {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_prompt {
  color: #303F9F;
  border-top: 1px solid transparent;
}
div.input_area > div.highlight {
  margin: 0.4em;
  border: none;
  padding: 0px;
  background-color: transparent;
}
div.input_area > div.highlight > pre {
  margin: 0px;
  border: none;
  padding: 0px;
  background-color: transparent;
}
/* The following gets added to the <head> if it is detected that the user has a
 * monospace font with inconsistent normal/bold/italic height.  See
 * notebookmain.js.  Such fonts will have keywords vertically offset with
 * respect to the rest of the text.  The user should select a better font.
 * See: https://github.com/ipython/ipython/issues/1503
 *
 * .CodeMirror span {
 *      vertical-align: bottom;
 * }
 */
.CodeMirror {
  line-height: 1.21429em;
  /* Changed from 1em to our global default */
  font-size: 14px;
  height: auto;
  /* Changed to auto to autogrow */
  background: none;
  /* Changed from white to allow our bg to show through */
}
.CodeMirror-scroll {
  /*  The CodeMirror docs are a bit fuzzy on if overflow-y should be hidden or visible.*/
  /*  We have found that if it is visible, vertical scrollbars appear with font size changes.*/
  overflow-y: hidden;
  overflow-x: auto;
}
.CodeMirror-lines {
  /* In CM2, this used to be 0.4em, but in CM3 it went to 4px. We need the em value because */
  /* we have set a different line-height and want this to scale with that. */
  /* Note that this should set vertical padding only, since CodeMirror assumes
       that horizontal padding will be set on CodeMirror pre */
  padding: 0.4em 0;
}
.CodeMirror-linenumber {
  padding: 0 8px 0 4px;
}
.CodeMirror-gutters {
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.CodeMirror pre {
  /* In CM3 this went to 4px from 0 in CM2. This sets horizontal padding only,
    use .CodeMirror-lines for vertical */
  padding: 0 0.4em;
  border: 0;
  border-radius: 0;
}
.CodeMirror-cursor {
  border-left: 1.4px solid black;
}
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .CodeMirror-cursor {
    border-left: 2px solid black;
  }
}
@media screen and (min-width: 4320px) {
  .CodeMirror-cursor {
    border-left: 4px solid black;
  }
}
/*

Original style from softwaremaniacs.org (c) Ivan Sagalaev <Maniac@SoftwareManiacs.Org>
Adapted from GitHub theme

*/
.highlight-base {
  color: #000;
}
.highlight-variable {
  color: #000;
}
.highlight-variable-2 {
  color: #1a1a1a;
}
.highlight-variable-3 {
  color: #333333;
}
.highlight-string {
  color: #BA2121;
}
.highlight-comment {
  color: #408080;
  font-style: italic;
}
.highlight-number {
  color: #080;
}
.highlight-atom {
  color: #88F;
}
.highlight-keyword {
  color: #008000;
  font-weight: bold;
}
.highlight-builtin {
  color: #008000;
}
.highlight-error {
  color: #f00;
}
.highlight-operator {
  color: #AA22FF;
  font-weight: bold;
}
.highlight-meta {
  color: #AA22FF;
}
/* previously not defined, copying from default codemirror */
.highlight-def {
  color: #00f;
}
.highlight-string-2 {
  color: #f50;
}
.highlight-qualifier {
  color: #555;
}
.highlight-bracket {
  color: #997;
}
.highlight-tag {
  color: #170;
}
.highlight-attribute {
  color: #00c;
}
.highlight-header {
  color: blue;
}
.highlight-quote {
  color: #090;
}
.highlight-link {
  color: #00c;
}
/* apply the same style to codemirror */
.cm-s-ipython span.cm-keyword {
  color: #008000;
  font-weight: bold;
}
.cm-s-ipython span.cm-atom {
  color: #88F;
}
.cm-s-ipython span.cm-number {
  color: #080;
}
.cm-s-ipython span.cm-def {
  color: #00f;
}
.cm-s-ipython span.cm-variable {
  color: #000;
}
.cm-s-ipython span.cm-operator {
  color: #AA22FF;
  font-weight: bold;
}
.cm-s-ipython span.cm-variable-2 {
  color: #1a1a1a;
}
.cm-s-ipython span.cm-variable-3 {
  color: #333333;
}
.cm-s-ipython span.cm-comment {
  color: #408080;
  font-style: italic;
}
.cm-s-ipython span.cm-string {
  color: #BA2121;
}
.cm-s-ipython span.cm-string-2 {
  color: #f50;
}
.cm-s-ipython span.cm-meta {
  color: #AA22FF;
}
.cm-s-ipython span.cm-qualifier {
  color: #555;
}
.cm-s-ipython span.cm-builtin {
  color: #008000;
}
.cm-s-ipython span.cm-bracket {
  color: #997;
}
.cm-s-ipython span.cm-tag {
  color: #170;
}
.cm-s-ipython span.cm-attribute {
  color: #00c;
}
.cm-s-ipython span.cm-header {
  color: blue;
}
.cm-s-ipython span.cm-quote {
  color: #090;
}
.cm-s-ipython span.cm-link {
  color: #00c;
}
.cm-s-ipython span.cm-error {
  color: #f00;
}
.cm-s-ipython span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}
div.output_wrapper {
  /* this position must be relative to enable descendents to be absolute within it */
  position: relative;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  z-index: 1;
}
/* class for the output area when it should be height-limited */
div.output_scroll {
  /* ideally, this would be max-height, but FF barfs all over that */
  height: 24em;
  /* FF needs this *and the wrapper* to specify full width, or it will shrinkwrap */
  width: 100%;
  overflow: auto;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  display: block;
}
/* output div while it is collapsed */
div.output_collapsed {
  margin: 0px;
  padding: 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
div.out_prompt_overlay {
  height: 100%;
  padding: 0px 0.4em;
  position: absolute;
  border-radius: 2px;
}
div.out_prompt_overlay:hover {
  /* use inner shadow to get border that is computed the same on WebKit/FF */
  -webkit-box-shadow: inset 0 0 1px #000;
  box-shadow: inset 0 0 1px #000;
  background: rgba(240, 240, 240, 0.5);
}
div.output_prompt {
  color: #D84315;
}
/* This class is the outer container of all output sections. */
div.output_area {
  padding: 0px;
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.output_area .MathJax_Display {
  text-align: left !important;
}
div.output_area .rendered_html table {
  margin-left: 0;
  margin-right: 0;
}
div.output_area .rendered_html img {
  margin-left: 0;
  margin-right: 0;
}
div.output_area img,
div.output_area svg {
  max-width: 100%;
  height: auto;
}
div.output_area img.unconfined,
div.output_area svg.unconfined {
  max-width: none;
}
div.output_area .mglyph > img {
  max-width: none;
}
/* This is needed to protect the pre formating from global settings such
   as that of bootstrap */
.output {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.output_area {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
div.output_area pre {
  margin: 0;
  padding: 1px 0 1px 0;
  border: 0;
  vertical-align: baseline;
  color: black;
  background-color: transparent;
  border-radius: 0;
}
/* This class is for the output subarea inside the output_area and after
   the prompt div. */
div.output_subarea {
  overflow-x: auto;
  padding: 0.4em;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
  max-width: calc(100% - 14ex);
}
div.output_scroll div.output_subarea {
  overflow-x: visible;
}
/* The rest of the output_* classes are for special styling of the different
   output types */
/* all text output has this class: */
div.output_text {
  text-align: left;
  color: #000;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
}
/* stdout/stderr are 'text' as well as 'stream', but execute_result/error are *not* streams */
div.output_stderr {
  background: #fdd;
  /* very light red background for stderr */
}
div.output_latex {
  text-align: left;
}
/* Empty output_javascript divs should have no height */
div.output_javascript:empty {
  padding: 0;
}
.js-error {
  color: darkred;
}
/* raw_input styles */
div.raw_input_container {
  line-height: 1.21429em;
  padding-top: 5px;
}
pre.raw_input_prompt {
  /* nothing needed here. */
}
input.raw_input {
  font-family: monospace;
  font-size: inherit;
  color: inherit;
  width: auto;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
}
input.raw_input:focus {
  box-shadow: none;
}
p.p-space {
  margin-bottom: 10px;
}
div.output_unrecognized {
  padding: 5px;
  font-weight: bold;
  color: red;
}
div.output_unrecognized a {
  color: inherit;
  text-decoration: none;
}
div.output_unrecognized a:hover {
  color: inherit;
  text-decoration: none;
}
.rendered_html {
  color: #000;
  /* any extras will just be numbers: */
}
.rendered_html em {
  font-style: italic;
}
.rendered_html strong {
  font-weight: bold;
}
.rendered_html u {
  text-decoration: underline;
}
.rendered_html :link {
  text-decoration: underline;
}
.rendered_html :visited {
  text-decoration: underline;
}
.rendered_html h1 {
  font-size: 185.7%;
  margin: 1.08em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h2 {
  font-size: 157.1%;
  margin: 1.27em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h3 {
  font-size: 128.6%;
  margin: 1.55em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h4 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h5 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h6 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h1:first-child {
  margin-top: 0.538em;
}
.rendered_html h2:first-child {
  margin-top: 0.636em;
}
.rendered_html h3:first-child {
  margin-top: 0.777em;
}
.rendered_html h4:first-child {
  margin-top: 1em;
}
.rendered_html h5:first-child {
  margin-top: 1em;
}
.rendered_html h6:first-child {
  margin-top: 1em;
}
.rendered_html ul:not(.list-inline),
.rendered_html ol:not(.list-inline) {
  padding-left: 2em;
}
.rendered_html ul {
  list-style: disc;
}
.rendered_html ul ul {
  list-style: square;
  margin-top: 0;
}
.rendered_html ul ul ul {
  list-style: circle;
}
.rendered_html ol {
  list-style: decimal;
}
.rendered_html ol ol {
  list-style: upper-alpha;
  margin-top: 0;
}
.rendered_html ol ol ol {
  list-style: lower-alpha;
}
.rendered_html ol ol ol ol {
  list-style: lower-roman;
}
.rendered_html ol ol ol ol ol {
  list-style: decimal;
}
.rendered_html * + ul {
  margin-top: 1em;
}
.rendered_html * + ol {
  margin-top: 1em;
}
.rendered_html hr {
  color: black;
  background-color: black;
}
.rendered_html pre {
  margin: 1em 2em;
  padding: 0px;
  background-color: #fff;
}
.rendered_html code {
  background-color: #eff0f1;
}
.rendered_html p code {
  padding: 1px 5px;
}
.rendered_html pre code {
  background-color: #fff;
}
.rendered_html pre,
.rendered_html code {
  border: 0;
  color: #000;
  font-size: 100%;
}
.rendered_html blockquote {
  margin: 1em 2em;
}
.rendered_html table {
  margin-left: auto;
  margin-right: auto;
  border: none;
  border-collapse: collapse;
  border-spacing: 0;
  color: black;
  font-size: 12px;
  table-layout: fixed;
}
.rendered_html thead {
  border-bottom: 1px solid black;
  vertical-align: bottom;
}
.rendered_html tr,
.rendered_html th,
.rendered_html td {
  text-align: right;
  vertical-align: middle;
  padding: 0.5em 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}
.rendered_html th {
  font-weight: bold;
}
.rendered_html tbody tr:nth-child(odd) {
  background: #f5f5f5;
}
.rendered_html tbody tr:hover {
  background: rgba(66, 165, 245, 0.2);
}
.rendered_html * + table {
  margin-top: 1em;
}
.rendered_html p {
  text-align: left;
}
.rendered_html * + p {
  margin-top: 1em;
}
.rendered_html img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.rendered_html * + img {
  margin-top: 1em;
}
.rendered_html img,
.rendered_html svg {
  max-width: 100%;
  height: auto;
}
.rendered_html img.unconfined,
.rendered_html svg.unconfined {
  max-width: none;
}
.rendered_html .alert {
  margin-bottom: initial;
}
.rendered_html * + .alert {
  margin-top: 1em;
}
[dir="rtl"] .rendered_html p {
  text-align: right;
}
div.text_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.text_cell > div.prompt {
    display: none;
  }
}
div.text_cell_render {
  /*font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;*/
  outline: none;
  resize: none;
  width: inherit;
  border-style: none;
  padding: 0.5em 0.5em 0.5em 0.4em;
  color: #000;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
a.anchor-link:link {
  text-decoration: none;
  padding: 0px 20px;
  visibility: hidden;
}
h1:hover .anchor-link,
h2:hover .anchor-link,
h3:hover .anchor-link,
h4:hover .anchor-link,
h5:hover .anchor-link,
h6:hover .anchor-link {
  visibility: visible;
}
.text_cell.rendered .input_area {
  display: none;
}
.text_cell.rendered .rendered_html {
  overflow-x: auto;
  overflow-y: hidden;
}
.text_cell.rendered .rendered_html tr,
.text_cell.rendered .rendered_html th,
.text_cell.rendered .rendered_html td {
  max-width: none;
}
.text_cell.unrendered .text_cell_render {
  display: none;
}
.text_cell .dropzone .input_area {
  border: 2px dashed #bababa;
  margin: -1px;
}
.cm-header-1,
.cm-header-2,
.cm-header-3,
.cm-header-4,
.cm-header-5,
.cm-header-6 {
  font-weight: bold;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.cm-header-1 {
  font-size: 185.7%;
}
.cm-header-2 {
  font-size: 157.1%;
}
.cm-header-3 {
  font-size: 128.6%;
}
.cm-header-4 {
  font-size: 110%;
}
.cm-header-5 {
  font-size: 100%;
  font-style: italic;
}
.cm-header-6 {
  font-size: 100%;
  font-style: italic;
}
/*!
*
* IPython notebook webapp
*
*/
@media (max-width: 767px) {
  .notebook_app {
    padding-left: 0px;
    padding-right: 0px;
  }
}
#ipython-main-app {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook_panel {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook {
  font-size: 14px;
  line-height: 20px;
  overflow-y: hidden;
  overflow-x: auto;
  width: 100%;
  /* This spaces the page away from the edge of the notebook area */
  padding-top: 20px;
  margin: 0px;
  outline: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  min-height: 100%;
}
@media not print {
  #notebook-container {
    padding: 15px;
    background-color: #fff;
    min-height: 0;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
@media print {
  #notebook-container {
    width: 100%;
  }
}
div.ui-widget-content {
  border: 1px solid #ababab;
  outline: none;
}
pre.dialog {
  background-color: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 2px;
  padding: 0.4em;
  padding-left: 2em;
}
p.dialog {
  padding: 0.2em;
}
/* Word-wrap output correctly.  This is the CSS3 spelling, though Firefox seems
   to not honor it correctly.  Webkit browsers (Chrome, rekonq, Safari) do.
 */
pre,
code,
kbd,
samp {
  white-space: pre-wrap;
}
#fonttest {
  font-family: monospace;
}
p {
  margin-bottom: 0;
}
.end_space {
  min-height: 100px;
  transition: height .2s ease;
}
.notebook_app > #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
@media not print {
  .notebook_app {
    background-color: #EEE;
  }
}
kbd {
  border-style: solid;
  border-width: 1px;
  box-shadow: none;
  margin: 2px;
  padding-left: 2px;
  padding-right: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
.jupyter-keybindings {
  padding: 1px;
  line-height: 24px;
  border-bottom: 1px solid gray;
}
.jupyter-keybindings input {
  margin: 0;
  padding: 0;
  border: none;
}
.jupyter-keybindings i {
  padding: 6px;
}
.well code {
  background-color: #ffffff;
  border-color: #ababab;
  border-width: 1px;
  border-style: solid;
  padding: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
/* CSS for the cell toolbar */
.celltoolbar {
  border: thin solid #CFCFCF;
  border-bottom: none;
  background: #EEE;
  border-radius: 2px 2px 0px 0px;
  width: 100%;
  height: 29px;
  padding-right: 4px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
  display: -webkit-flex;
}
@media print {
  .celltoolbar {
    display: none;
  }
}
.ctb_hideshow {
  display: none;
  vertical-align: bottom;
}
/* ctb_show is added to the ctb_hideshow div to show the cell toolbar.
   Cell toolbars are only shown when the ctb_global_show class is also set.
*/
.ctb_global_show .ctb_show.ctb_hideshow {
  display: block;
}
.ctb_global_show .ctb_show + .input_area,
.ctb_global_show .ctb_show + div.text_cell_input,
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border-top-right-radius: 0px;
  border-top-left-radius: 0px;
}
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border: 1px solid #cfcfcf;
}
.celltoolbar {
  font-size: 87%;
  padding-top: 3px;
}
.celltoolbar select {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  width: inherit;
  font-size: inherit;
  height: 22px;
  padding: 0px;
  display: inline-block;
}
.celltoolbar select:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.celltoolbar select::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.celltoolbar select:-ms-input-placeholder {
  color: #999;
}
.celltoolbar select::-webkit-input-placeholder {
  color: #999;
}
.celltoolbar select::-ms-expand {
  border: 0;
  background-color: transparent;
}
.celltoolbar select[disabled],
.celltoolbar select[readonly],
fieldset[disabled] .celltoolbar select {
  background-color: #eeeeee;
  opacity: 1;
}
.celltoolbar select[disabled],
fieldset[disabled] .celltoolbar select {
  cursor: not-allowed;
}
textarea.celltoolbar select {
  height: auto;
}
select.celltoolbar select {
  height: 30px;
  line-height: 30px;
}
textarea.celltoolbar select,
select[multiple].celltoolbar select {
  height: auto;
}
.celltoolbar label {
  margin-left: 5px;
  margin-right: 5px;
}
.tags_button_container {
  width: 100%;
  display: flex;
}
.tag-container {
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  overflow: hidden;
  position: relative;
}
.tag-container > * {
  margin: 0 4px;
}
.remove-tag-btn {
  margin-left: 4px;
}
.tags-input {
  display: flex;
}
.cell-tag:last-child:after {
  content: "";
  position: absolute;
  right: 0;
  width: 40px;
  height: 100%;
  /* Fade to background color of cell toolbar */
  background: linear-gradient(to right, rgba(0, 0, 0, 0), #EEE);
}
.tags-input > * {
  margin-left: 4px;
}
.cell-tag,
.tags-input input,
.tags-input button {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  box-shadow: none;
  width: inherit;
  font-size: inherit;
  height: 22px;
  line-height: 22px;
  padding: 0px 4px;
  display: inline-block;
}
.cell-tag:focus,
.tags-input input:focus,
.tags-input button:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.cell-tag::-moz-placeholder,
.tags-input input::-moz-placeholder,
.tags-input button::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.cell-tag:-ms-input-placeholder,
.tags-input input:-ms-input-placeholder,
.tags-input button:-ms-input-placeholder {
  color: #999;
}
.cell-tag::-webkit-input-placeholder,
.tags-input input::-webkit-input-placeholder,
.tags-input button::-webkit-input-placeholder {
  color: #999;
}
.cell-tag::-ms-expand,
.tags-input input::-ms-expand,
.tags-input button::-ms-expand {
  border: 0;
  background-color: transparent;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
.cell-tag[readonly],
.tags-input input[readonly],
.tags-input button[readonly],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  background-color: #eeeeee;
  opacity: 1;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  cursor: not-allowed;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button {
  height: auto;
}
select.cell-tag,
select.tags-input input,
select.tags-input button {
  height: 30px;
  line-height: 30px;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button,
select[multiple].cell-tag,
select[multiple].tags-input input,
select[multiple].tags-input button {
  height: auto;
}
.cell-tag,
.tags-input button {
  padding: 0px 4px;
}
.cell-tag {
  background-color: #fff;
  white-space: nowrap;
}
.tags-input input[type=text]:focus {
  outline: none;
  box-shadow: none;
  border-color: #ccc;
}
.completions {
  position: absolute;
  z-index: 110;
  overflow: hidden;
  border: 1px solid #ababab;
  border-radius: 2px;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  line-height: 1;
}
.completions select {
  background: white;
  outline: none;
  border: none;
  padding: 0px;
  margin: 0px;
  overflow: auto;
  font-family: monospace;
  font-size: 110%;
  color: #000;
  width: auto;
}
.completions select option.context {
  color: #286090;
}
#kernel_logo_widget .current_kernel_logo {
  display: none;
  margin-top: -1px;
  margin-bottom: -1px;
  width: 32px;
  height: 32px;
}
[dir="rtl"] #kernel_logo_widget {
  float: left !important;
  float: left;
}
.modal .modal-body .move-path {
  display: flex;
  flex-direction: row;
  justify-content: space;
  align-items: center;
}
.modal .modal-body .move-path .server-root {
  padding-right: 20px;
}
.modal .modal-body .move-path .path-input {
  flex: 1;
}
#menubar {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  margin-top: 1px;
}
#menubar .navbar {
  border-top: 1px;
  border-radius: 0px 0px 2px 2px;
  margin-bottom: 0px;
}
#menubar .navbar-toggle {
  float: left;
  padding-top: 7px;
  padding-bottom: 7px;
  border: none;
}
#menubar .navbar-collapse {
  clear: left;
}
[dir="rtl"] #menubar .navbar-toggle {
  float: right;
}
[dir="rtl"] #menubar .navbar-collapse {
  clear: right;
}
[dir="rtl"] #menubar .navbar-nav {
  float: right;
}
[dir="rtl"] #menubar .nav {
  padding-right: 0px;
}
[dir="rtl"] #menubar .navbar-nav > li {
  float: right;
}
[dir="rtl"] #menubar .navbar-right {
  float: left !important;
}
[dir="rtl"] ul.dropdown-menu {
  text-align: right;
  left: auto;
}
[dir="rtl"] ul#new-menu.dropdown-menu {
  right: auto;
  left: 0;
}
.nav-wrapper {
  border-bottom: 1px solid #e7e7e7;
}
i.menu-icon {
  padding-top: 4px;
}
[dir="rtl"] i.menu-icon.pull-right {
  float: left !important;
  float: left;
}
ul#help_menu li a {
  overflow: hidden;
  padding-right: 2.2em;
}
ul#help_menu li a i {
  margin-right: -1.2em;
}
[dir="rtl"] ul#help_menu li a {
  padding-left: 2.2em;
}
[dir="rtl"] ul#help_menu li a i {
  margin-right: 0;
  margin-left: -1.2em;
}
[dir="rtl"] ul#help_menu li a i.pull-right {
  float: left !important;
  float: left;
}
.dropdown-submenu {
  position: relative;
}
.dropdown-submenu > .dropdown-menu {
  top: 0;
  left: 100%;
  margin-top: -6px;
  margin-left: -1px;
}
[dir="rtl"] .dropdown-submenu > .dropdown-menu {
  right: 100%;
  margin-right: -1px;
}
.dropdown-submenu:hover > .dropdown-menu {
  display: block;
}
.dropdown-submenu > a:after {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: block;
  content: "\f0da";
  float: right;
  color: #333333;
  margin-top: 2px;
  margin-right: -10px;
}
.dropdown-submenu > a:after.fa-pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.fa-pull-right {
  margin-left: .3em;
}
.dropdown-submenu > a:after.pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.pull-right {
  margin-left: .3em;
}
[dir="rtl"] .dropdown-submenu > a:after {
  float: left;
  content: "\f0d9";
  margin-right: 0;
  margin-left: -10px;
}
.dropdown-submenu:hover > a:after {
  color: #262626;
}
.dropdown-submenu.pull-left {
  float: none;
}
.dropdown-submenu.pull-left > .dropdown-menu {
  left: -100%;
  margin-left: 10px;
}
#notification_area {
  float: right !important;
  float: right;
  z-index: 10;
}
[dir="rtl"] #notification_area {
  float: left !important;
  float: left;
}
.indicator_area {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] .indicator_area {
  float: left !important;
  float: left;
}
#kernel_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  border-left: 1px solid;
}
#kernel_indicator .kernel_indicator_name {
  padding-left: 5px;
  padding-right: 5px;
}
[dir="rtl"] #kernel_indicator {
  float: left !important;
  float: left;
  border-left: 0;
  border-right: 1px solid;
}
#modal_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] #modal_indicator {
  float: left !important;
  float: left;
}
#readonly-indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  margin-top: 2px;
  margin-bottom: 0px;
  margin-left: 0px;
  margin-right: 0px;
  display: none;
}
.modal_indicator:before {
  width: 1.28571429em;
  text-align: center;
}
.edit_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f040";
}
.edit_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.edit_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: ' ';
}
.command_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f10c";
}
.kernel_idle_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f111";
}
.kernel_busy_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f1e2";
}
.kernel_dead_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f127";
}
.kernel_disconnected_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.pull-right {
  margin-left: .3em;
}
.notification_widget {
  color: #777;
  z-index: 10;
  background: rgba(240, 240, 240, 0.5);
  margin-right: 4px;
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget:focus,
.notification_widget.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.notification_widget:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active:hover,
.notification_widget.active:hover,
.open > .dropdown-toggle.notification_widget:hover,
.notification_widget:active:focus,
.notification_widget.active:focus,
.open > .dropdown-toggle.notification_widget:focus,
.notification_widget:active.focus,
.notification_widget.active.focus,
.open > .dropdown-toggle.notification_widget.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  background-image: none;
}
.notification_widget.disabled:hover,
.notification_widget[disabled]:hover,
fieldset[disabled] .notification_widget:hover,
.notification_widget.disabled:focus,
.notification_widget[disabled]:focus,
fieldset[disabled] .notification_widget:focus,
.notification_widget.disabled.focus,
.notification_widget[disabled].focus,
fieldset[disabled] .notification_widget.focus {
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget .badge {
  color: #fff;
  background-color: #333;
}
.notification_widget.warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning:focus,
.notification_widget.warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.notification_widget.warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active:hover,
.notification_widget.warning.active:hover,
.open > .dropdown-toggle.notification_widget.warning:hover,
.notification_widget.warning:active:focus,
.notification_widget.warning.active:focus,
.open > .dropdown-toggle.notification_widget.warning:focus,
.notification_widget.warning:active.focus,
.notification_widget.warning.active.focus,
.open > .dropdown-toggle.notification_widget.warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  background-image: none;
}
.notification_widget.warning.disabled:hover,
.notification_widget.warning[disabled]:hover,
fieldset[disabled] .notification_widget.warning:hover,
.notification_widget.warning.disabled:focus,
.notification_widget.warning[disabled]:focus,
fieldset[disabled] .notification_widget.warning:focus,
.notification_widget.warning.disabled.focus,
.notification_widget.warning[disabled].focus,
fieldset[disabled] .notification_widget.warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.notification_widget.success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success:focus,
.notification_widget.success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.notification_widget.success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active:hover,
.notification_widget.success.active:hover,
.open > .dropdown-toggle.notification_widget.success:hover,
.notification_widget.success:active:focus,
.notification_widget.success.active:focus,
.open > .dropdown-toggle.notification_widget.success:focus,
.notification_widget.success:active.focus,
.notification_widget.success.active.focus,
.open > .dropdown-toggle.notification_widget.success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  background-image: none;
}
.notification_widget.success.disabled:hover,
.notification_widget.success[disabled]:hover,
fieldset[disabled] .notification_widget.success:hover,
.notification_widget.success.disabled:focus,
.notification_widget.success[disabled]:focus,
fieldset[disabled] .notification_widget.success:focus,
.notification_widget.success.disabled.focus,
.notification_widget.success[disabled].focus,
fieldset[disabled] .notification_widget.success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.notification_widget.info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info:focus,
.notification_widget.info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.notification_widget.info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active:hover,
.notification_widget.info.active:hover,
.open > .dropdown-toggle.notification_widget.info:hover,
.notification_widget.info:active:focus,
.notification_widget.info.active:focus,
.open > .dropdown-toggle.notification_widget.info:focus,
.notification_widget.info:active.focus,
.notification_widget.info.active.focus,
.open > .dropdown-toggle.notification_widget.info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  background-image: none;
}
.notification_widget.info.disabled:hover,
.notification_widget.info[disabled]:hover,
fieldset[disabled] .notification_widget.info:hover,
.notification_widget.info.disabled:focus,
.notification_widget.info[disabled]:focus,
fieldset[disabled] .notification_widget.info:focus,
.notification_widget.info.disabled.focus,
.notification_widget.info[disabled].focus,
fieldset[disabled] .notification_widget.info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.notification_widget.danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger:focus,
.notification_widget.danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.notification_widget.danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active:hover,
.notification_widget.danger.active:hover,
.open > .dropdown-toggle.notification_widget.danger:hover,
.notification_widget.danger:active:focus,
.notification_widget.danger.active:focus,
.open > .dropdown-toggle.notification_widget.danger:focus,
.notification_widget.danger:active.focus,
.notification_widget.danger.active.focus,
.open > .dropdown-toggle.notification_widget.danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  background-image: none;
}
.notification_widget.danger.disabled:hover,
.notification_widget.danger[disabled]:hover,
fieldset[disabled] .notification_widget.danger:hover,
.notification_widget.danger.disabled:focus,
.notification_widget.danger[disabled]:focus,
fieldset[disabled] .notification_widget.danger:focus,
.notification_widget.danger.disabled.focus,
.notification_widget.danger[disabled].focus,
fieldset[disabled] .notification_widget.danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger .badge {
  color: #d9534f;
  background-color: #fff;
}
div#pager {
  background-color: #fff;
  font-size: 14px;
  line-height: 20px;
  overflow: hidden;
  display: none;
  position: fixed;
  bottom: 0px;
  width: 100%;
  max-height: 50%;
  padding-top: 8px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  /* Display over codemirror */
  z-index: 100;
  /* Hack which prevents jquery ui resizable from changing top. */
  top: auto !important;
}
div#pager pre {
  line-height: 1.21429em;
  color: #000;
  background-color: #f7f7f7;
  padding: 0.4em;
}
div#pager #pager-button-area {
  position: absolute;
  top: 8px;
  right: 20px;
}
div#pager #pager-contents {
  position: relative;
  overflow: auto;
  width: 100%;
  height: 100%;
}
div#pager #pager-contents #pager-container {
  position: relative;
  padding: 15px 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
div#pager .ui-resizable-handle {
  top: 0px;
  height: 8px;
  background: #f7f7f7;
  border-top: 1px solid #cfcfcf;
  border-bottom: 1px solid #cfcfcf;
  /* This injects handle bars (a short, wide = symbol) for 
        the resize handle. */
}
div#pager .ui-resizable-handle::after {
  content: '';
  top: 2px;
  left: 50%;
  height: 3px;
  width: 30px;
  margin-left: -15px;
  position: absolute;
  border-top: 1px solid #cfcfcf;
}
.quickhelp {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  line-height: 1.8em;
}
.shortcut_key {
  display: inline-block;
  width: 21ex;
  text-align: right;
  font-family: monospace;
}
.shortcut_descr {
  display: inline-block;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
span.save_widget {
  height: 30px;
  margin-top: 4px;
  display: flex;
  justify-content: flex-start;
  align-items: baseline;
  width: 50%;
  flex: 1;
}
span.save_widget span.filename {
  height: 100%;
  line-height: 1em;
  margin-left: 16px;
  border: none;
  font-size: 146.5%;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
  border-radius: 2px;
}
span.save_widget span.filename:hover {
  background-color: #e6e6e6;
}
[dir="rtl"] span.save_widget.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] span.save_widget span.filename {
  margin-left: 0;
  margin-right: 16px;
}
span.checkpoint_status,
span.autosave_status {
  font-size: small;
  white-space: nowrap;
  padding: 0 5px;
}
@media (max-width: 767px) {
  span.save_widget {
    font-size: small;
    padding: 0 0 0 5px;
  }
  span.checkpoint_status,
  span.autosave_status {
    display: none;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  span.checkpoint_status {
    display: none;
  }
  span.autosave_status {
    font-size: x-small;
  }
}
.toolbar {
  padding: 0px;
  margin-left: -5px;
  margin-top: 2px;
  margin-bottom: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.toolbar select,
.toolbar label {
  width: auto;
  vertical-align: middle;
  margin-right: 2px;
  margin-bottom: 0px;
  display: inline;
  font-size: 92%;
  margin-left: 0.3em;
  margin-right: 0.3em;
  padding: 0px;
  padding-top: 3px;
}
.toolbar .btn {
  padding: 2px 8px;
}
.toolbar .btn-group {
  margin-top: 0px;
  margin-left: 5px;
}
.toolbar-btn-label {
  margin-left: 6px;
}
#maintoolbar {
  margin-bottom: -3px;
  margin-top: -8px;
  border: 0px;
  min-height: 27px;
  margin-left: 0px;
  padding-top: 11px;
  padding-bottom: 3px;
}
#maintoolbar .navbar-text {
  float: none;
  vertical-align: middle;
  text-align: right;
  margin-left: 5px;
  margin-right: 0px;
  margin-top: 0px;
}
.select-xs {
  height: 24px;
}
[dir="rtl"] .btn-group > .btn,
.btn-group-vertical > .btn {
  float: right;
}
.pulse,
.dropdown-menu > li > a.pulse,
li.pulse > a.dropdown-toggle,
li.pulse.open > a.dropdown-toggle {
  background-color: #F37626;
  color: white;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
/** WARNING IF YOU ARE EDITTING THIS FILE, if this is a .css file, It has a lot
 * of chance of beeing generated from the ../less/[samename].less file, you can
 * try to get back the less file by reverting somme commit in history
 **/
/*
 * We'll try to get something pretty, so we
 * have some strange css to have the scroll bar on
 * the left with fix button on the top right of the tooltip
 */
@-moz-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-webkit-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-moz-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-webkit-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
/*properties of tooltip after "expand"*/
.bigtooltip {
  overflow: auto;
  height: 200px;
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
}
/*properties of tooltip before "expand"*/
.smalltooltip {
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
  text-overflow: ellipsis;
  overflow: hidden;
  height: 80px;
}
.tooltipbuttons {
  position: absolute;
  padding-right: 15px;
  top: 0px;
  right: 0px;
}
.tooltiptext {
  /*avoid the button to overlap on some docstring*/
  padding-right: 30px;
}
.ipython_tooltip {
  max-width: 700px;
  /*fade-in animation when inserted*/
  -webkit-animation: fadeOut 400ms;
  -moz-animation: fadeOut 400ms;
  animation: fadeOut 400ms;
  -webkit-animation: fadeIn 400ms;
  -moz-animation: fadeIn 400ms;
  animation: fadeIn 400ms;
  vertical-align: middle;
  background-color: #f7f7f7;
  overflow: visible;
  border: #ababab 1px solid;
  outline: none;
  padding: 3px;
  margin: 0px;
  padding-left: 7px;
  font-family: monospace;
  min-height: 50px;
  -moz-box-shadow: 0px 6px 10px -1px #adadad;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  border-radius: 2px;
  position: absolute;
  z-index: 1000;
}
.ipython_tooltip a {
  float: right;
}
.ipython_tooltip .tooltiptext pre {
  border: 0;
  border-radius: 0;
  font-size: 100%;
  background-color: #f7f7f7;
}
.pretooltiparrow {
  left: 0px;
  margin: 0px;
  top: -16px;
  width: 40px;
  height: 16px;
  overflow: hidden;
  position: absolute;
}
.pretooltiparrow:before {
  background-color: #f7f7f7;
  border: 1px #ababab solid;
  z-index: 11;
  content: "";
  position: absolute;
  left: 15px;
  top: 10px;
  width: 25px;
  height: 25px;
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  -o-transform: rotate(45deg);
}
ul.typeahead-list i {
  margin-left: -10px;
  width: 18px;
}
[dir="rtl"] ul.typeahead-list i {
  margin-left: 0;
  margin-right: -10px;
}
ul.typeahead-list {
  max-height: 80vh;
  overflow: auto;
}
ul.typeahead-list > li > a {
  /** Firefox bug **/
  /* see https://github.com/jupyter/notebook/issues/559 */
  white-space: normal;
}
ul.typeahead-list  > li > a.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .typeahead-list {
  text-align: right;
}
.cmd-palette .modal-body {
  padding: 7px;
}
.cmd-palette form {
  background: white;
}
.cmd-palette input {
  outline: none;
}
.no-shortcut {
  min-width: 20px;
  color: transparent;
}
[dir="rtl"] .no-shortcut.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .command-shortcut.pull-right {
  float: left !important;
  float: left;
}
.command-shortcut:before {
  content: "(command mode)";
  padding-right: 3px;
  color: #777777;
}
.edit-shortcut:before {
  content: "(edit)";
  padding-right: 3px;
  color: #777777;
}
[dir="rtl"] .edit-shortcut.pull-right {
  float: left !important;
  float: left;
}
#find-and-replace #replace-preview .match,
#find-and-replace #replace-preview .insert {
  background-color: #BBDEFB;
  border-color: #90CAF9;
  border-style: solid;
  border-width: 1px;
  border-radius: 0px;
}
[dir="ltr"] #find-and-replace .input-group-btn + .form-control {
  border-left: none;
}
[dir="rtl"] #find-and-replace .input-group-btn + .form-control {
  border-right: none;
}
#find-and-replace #replace-preview .replace .match {
  background-color: #FFCDD2;
  border-color: #EF9A9A;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .insert {
  background-color: #C8E6C9;
  border-color: #A5D6A7;
  border-radius: 0px;
}
#find-and-replace #replace-preview {
  max-height: 60vh;
  overflow: auto;
}
#find-and-replace #replace-preview pre {
  padding: 5px 10px;
}
.terminal-app {
  background: #EEE;
}
.terminal-app #header {
  background: #fff;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.terminal-app .terminal {
  width: 100%;
  float: left;
  font-family: monospace;
  color: white;
  background: black;
  padding: 0.4em;
  border-radius: 2px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
}
.terminal-app .terminal,
.terminal-app .terminal dummy-screen {
  line-height: 1em;
  font-size: 14px;
}
.terminal-app .terminal .xterm-rows {
  padding: 10px;
}
.terminal-app .terminal-cursor {
  color: black;
  background: white;
}
.terminal-app #terminado-container {
  margin-top: 20px;
}
/*# sourceMappingURL=style.min.css.map */
    </style>
<style type="text/css">
    .highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sa { color: #BA2121 } /* Literal.String.Affix */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .dl { color: #BA2121 } /* Literal.String.Delimiter */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .fm { color: #0000FF } /* Name.Function.Magic */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .vm { color: #19177C } /* Name.Variable.Magic */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    </style>
<style type="text/css">
    
/* Temporary definitions which will become obsolete with Notebook release 5.0 */
.ansi-black-fg { color: #3E424D; }
.ansi-black-bg { background-color: #3E424D; }
.ansi-black-intense-fg { color: #282C36; }
.ansi-black-intense-bg { background-color: #282C36; }
.ansi-red-fg { color: #E75C58; }
.ansi-red-bg { background-color: #E75C58; }
.ansi-red-intense-fg { color: #B22B31; }
.ansi-red-intense-bg { background-color: #B22B31; }
.ansi-green-fg { color: #00A250; }
.ansi-green-bg { background-color: #00A250; }
.ansi-green-intense-fg { color: #007427; }
.ansi-green-intense-bg { background-color: #007427; }
.ansi-yellow-fg { color: #DDB62B; }
.ansi-yellow-bg { background-color: #DDB62B; }
.ansi-yellow-intense-fg { color: #B27D12; }
.ansi-yellow-intense-bg { background-color: #B27D12; }
.ansi-blue-fg { color: #208FFB; }
.ansi-blue-bg { background-color: #208FFB; }
.ansi-blue-intense-fg { color: #0065CA; }
.ansi-blue-intense-bg { background-color: #0065CA; }
.ansi-magenta-fg { color: #D160C4; }
.ansi-magenta-bg { background-color: #D160C4; }
.ansi-magenta-intense-fg { color: #A03196; }
.ansi-magenta-intense-bg { background-color: #A03196; }
.ansi-cyan-fg { color: #60C6C8; }
.ansi-cyan-bg { background-color: #60C6C8; }
.ansi-cyan-intense-fg { color: #258F8F; }
.ansi-cyan-intense-bg { background-color: #258F8F; }
.ansi-white-fg { color: #C5C1B4; }
.ansi-white-bg { background-color: #C5C1B4; }
.ansi-white-intense-fg { color: #A1A6B2; }
.ansi-white-intense-bg { background-color: #A1A6B2; }

.ansi-bold { font-weight: bold; }

    </style>


<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}

div#notebook {
  overflow: visible;
  border-top: none;
}@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  } 
  div.output_wrapper { 
    display: block;
    page-break-inside: avoid; 
  }
  div.output { 
    display: block;
    page-break-inside: avoid; 
  }
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

<!-- Loading mathjax macro -->
<!-- Load mathjax -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: true }
        }
    });
    </script>
    <!-- End of mathjax configuration --></head>
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Jakes-Fading-Simulation">Jakes Fading Simulation<a class="anchor-link" href="#Jakes-Fading-Simulation">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[190]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="o">%</span><span class="k">run</span> -i jakes.py
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Distribution-of-Doppler-shifts">Distribution of Doppler shifts<a class="anchor-link" href="#Distribution-of-Doppler-shifts">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[191]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">NN_bin</span> <span class="o">=</span> <span class="mi">32</span>
<span class="n">jakes_fading</span><span class="p">(</span>
    <span class="n">NN_sym</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span>
    <span class="n">NN_pth</span> <span class="o">=</span> <span class="n">NN_bin</span> <span class="o">*</span> <span class="mi">8192</span><span class="p">,</span>     <span class="c1"># Number of doppler shifts</span>
<span class="p">)</span>

<span class="n">fig</span><span class="p">,</span> <span class="n">axs</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">()</span>
<span class="n">axs</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="sa">r</span><span class="s2">&quot;Histogram of path doppler shift $\Xi$&quot;</span><span class="p">)</span>
<span class="n">axs</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="sa">r</span><span class="s2">&quot;$\xi$&quot;</span><span class="p">)</span>
<span class="n">axs</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="sa">r</span><span class="s2">&quot;count&quot;</span><span class="p">)</span>
<span class="n">axs</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">xi_l</span><span class="p">,</span><span class="n">bins</span> <span class="o">=</span> <span class="n">NN_bin</span><span class="p">)</span>

<span class="n">fig</span><span class="o">.</span><span class="n">tight_layout</span><span class="p">()</span>
<span class="n">fig</span><span class="o">.</span><span class="n">savefig</span><span class="p">(</span><span class="s2">&quot;./plots/doppler_shifts.png&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Fading-Envelope">Fading Envelope<a class="anchor-link" href="#Fading-Envelope">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[192]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">jakes_fading</span><span class="p">(</span>
    <span class="n">NN_sym</span> <span class="o">=</span>    <span class="mi">8</span><span class="p">,</span> <span class="c1"># number of symbols</span>
    <span class="n">NN_sps</span> <span class="o">=</span>  <span class="mi">256</span><span class="p">,</span> <span class="c1"># number of samples per symbol</span>
    <span class="n">NN_pth</span> <span class="o">=</span>    <span class="mi">8</span><span class="p">,</span> <span class="c1"># number of paths</span>
    <span class="n">FF_dop</span> <span class="o">=</span>    <span class="mi">1</span><span class="p">,</span> <span class="c1"># maximum doppler shift (Hz)</span>
    <span class="n">FF_car</span> <span class="o">=</span>    <span class="mi">0</span><span class="p">,</span> <span class="c1"># carrier frequency (Hz)</span>
    <span class="n">FF_sym</span> <span class="o">=</span>    <span class="mi">1</span><span class="p">,</span> <span class="c1"># symbol rate (baud)</span>
<span class="p">)</span>

<span class="n">fig</span><span class="p">,</span> <span class="n">axs</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">()</span>
<span class="n">axs</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="sa">r</span><span class="s2">&quot;Jakes fading envelope&quot;</span><span class="p">)</span>
<span class="n">axs</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="sa">r</span><span class="s2">&quot;normalized time $t/T$&quot;</span><span class="p">)</span>
<span class="n">axs</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="sa">r</span><span class="s2">&quot;magnitude&quot;</span><span class="p">)</span>
<span class="n">axs</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">tt_n</span><span class="o">/</span><span class="n">TT_sym</span><span class="p">,</span><span class="n">np</span><span class="o">.</span><span class="n">abs</span><span class="p">(</span><span class="n">xx_n</span><span class="p">))</span>
<span class="n">fig</span><span class="o">.</span><span class="n">savefig</span><span class="p">(</span><span class="s2">&quot;./plots/fading_envelope.png&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAYcAAAEWCAYAAACNJFuYAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4zLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvnQurowAAIABJREFUeJzsvWmQXNd5pvme3Pet9sJeAMF9A0GKpBaXJNBuS9E9HhuUxtMR0+0Im+of/jPjbnLc056J7miPTY0tT9sTlkg5rJiIaY9JUbbGsrUBFIsUxQ0ESAIEiK0KKNRemZX7vp35ce/JvJV1l3NvZiETqPNEVFRVZt6bJ7Oyzne/7f0IpRQCgUAgECix9XsBAoFAIBg8hHEQCAQCwRaEcRAIBALBFoRxEAgEAsEWhHEQCAQCwRaEcRAIBALBFoRxEAgEAsEWhHEQDAyEkGcJIc/r3B8hhJzu4fMdIYScIIScMHHMrPx9iv08aPT6fRLsTBz9XoBA0EeeB/A0pTRt9kBK6RyAg71fkkAwGAjPQbCTmbJiGASCnYAwDoKBhIV7CCGnCSERlfunCCEvyD8/Kz/uhBxSmVIcrxoyIoQ8C4A97ojecxJCXpBvewFATL6tFbphPyse97zi2OcV532BEPKM2lo61q96PkLId9la5d9n1Y5XOf8zijUcU1nzLHsvec4n2CFQSsWX+BqILwDPAni+47ZnALwg/xwBcFr+PgtgCsARACfk+6cAvAApXHSM4/lmNW5XPucxdn7595RyLYqfKYBIx2OmAHxX/ll1TRrr1zrfcfb+yMd9V+f408rHKZ6PvX8Rdl7F7cfUztfvz4X46s+XyDkIBhJCyBSkzeqpjruYgXieUjonX1XHCCHfle+fAvAcgBcIIa9A2tzmunjOpyBtwoykxuFztB2iUj6GXXlvKH5W8lWV9auej1L6ivx6n5OPe0nneMbX5McxTkJ6jSc71vkCJMMwZHA+wQ5BGAfBwCGHTr4N4HcAzEHa4Bhs838OwIvybc9RSk92nOMp+bjTAKJdPicPW3IXsvGKyaGtNKX06xrHblq/HMrRyoXMMSNGKX2OEPKoxvF6xAzu3/J+CnYeIucg6CsdG9lTkMJFRwG8RCk9g61XrmfkTfYF+Sr6JSg2cjnfMEUpnaOUPgfgfc64udZzngDwtGKtRhur8rVNAThJKX2KUvq0xsO2rN/gtC/Ij2fekNHx38VmQ3ccwMvyz8rX8jVI3oTZ9QhuU4TnIOg3Rwkhz0HaqJKU0hflDemEfPWfhkooh1L6dTkh/IL8WJZ4PgEgTQhhm7EyPKPHSbXnpJSeJIQ8LT/X+2hvyobInsOzhJDj8jlPygZL+ZgzHYnzE2h7RFrr/C5kg2V0vLz+I4q+h+copWlmMOXwETNiZ+TbOs+n5fEIbmMIpWLYj0CwHciezaxs8CKQwlYvUUpf6fPSmBd0mlIqejUEqoiwkkCwfUTQ9kDSkLwO7rCUQNBPhOcgEGwTCm+B5TzmKKVmE93bgvAcBEYI4yAQCASCLYiwkkAgEAi2cMtWKw0PD9P9+/dbOrZQKMDv9/d2QT1ArMscYl3mGNR1AYO7tttxXadPn05QSkcMH9jvFm2rX4888gi1ymuvvWb52O1ErMscYl3mGNR1UTq4a7sd1wXgfcqxx25bWIkQckxH9OyILPZ1ukNYLNUpXCYQCASCm8+2hZWo1HzznMbdMSpXSciyBaxJ6Wkq2vYFAoGg72xrtRIh5ASltFM4rfMxx6ncFCR3kp6hGkJpstzxMwAwNjb2yN/+7d9aWlc+n0cgELB07HYi1mUOsS5zDOq6gMFd2+24rs9//vOnKaVHDR/IE3uy+gWF1LHG/c90/g6pJtxQJljkHG4eYl3mEOsyz6Cu7XZcF/qdc+Bkk1dBKX2RSp2kadmLEAgEAkEf6Jtx6FTKlKdVMYOw0YclCQQCgUBmO6uVjkNS3DyuuE1ZvRTDZrXNlyF5DMcAabDJdq1NIBAIBPpsZ7XSKwBe6bjtKcXPmwaqyOEkVqkkKpZuIu/MbWA1U8Z/89AkCCH9Xo5AIBgAbtkOaUFvmI3n8ZvffgeUAtV6E195dE+/lyQQCAaAfiekBX3m5VMLsBOC0aAb//fb1/u9HIFAMCAI47DD+emFNTx5aBi/9ekDOL+cxXqu3O8lCQSCAUAYhx3Meq6Ma4kCPnfHMD59aAgA8O7clomcAoFgByKMww7m3GIGAPDgngjuGg/BaSe4sJLt86oEAsEgIIzDDubsYgY2Atw7GYLLYcPBkQA+EcZBIBBAGIcdzdV4HntjPvhcUtHaPRMhYRwEAgEAYRx2NNcTBewfbg8MOTgawFq2gmK13sdVCQSCQUAYhx0KpVQyDkNt47A35gMA3EgW+7UsgUAwIAjjsM18+405PP2ttwYuXBPPV1CoNrB/yNe6rWUcNoRxEAh2OsI4bCMfL2Xwhz/8BKeup/B7L3/EZMkHgusJyQAow0r7hoTnIBAIJIRx2Eb+5r0b8Dht+P1fvQsXVrL4cCFtfNBN4nqiAAA4oDAOYa8TQY9DGAeBQCCMA+Piahb/eHYZjWZvru4ppXj9Uhyfv3MU/91je2EjwGuX4j05dy9YTBVhI8BkxNu6jRCCPVEfFoRxEAh2PMI4QOoUfvqbb+N3/+YDfPvnqhNKTbOQLGEpXcKTB4cQ9jrxwO4I3rwyOMZhNVvGcMANp33zR2A87MFattKnVQkEgkFBGAcAf3dmCblKHWMhN77zi2s98R7O3EgBAB49EAMAPD41hHNLGVTrza7P3QtWsxVMhD1bbh8LeQZeXylTrCFXrvV7GQLBbY0wDgB+eG4FD+2J4Pd/9W6sZSs9qSy6uJqD005wcEQaAn7frhBqDYrLa7muz90LVjMljIXUjIMbiXx1YIxYJ3PxPJ7441fx+T95Hdnq4CT4BYLbjR1vHPKVOj5eyuBzh0fw5EFJfO6t2UTX5724msXBkUArbHPfZBgAcH450/W5e8FqpoxxDc8BkEpdB5Fv//waitUGEvkKZhaE9yAQbBc73jicXUijSYEjeyMYDXmwf8iH0/Oprs97aTWHuydCrd/3xnwIuB04t9R/41CqNpAt1zWMgxsAsJYdvNASpRSvXVzHlx+YwJG9EXy43uj3kgSC25Ydbxw+kpVJH9oTAQDcMxnCpdXuQj/Zcg0rmTIOjwVbt9lsBIfHAri6nu/q3L1gVd74x1XCSqNB6bb1ATQOs/ECVrNlfObQMD5zaBjXMk3kK0LqQyDYDna8cbi6nsdYyI2IzwUAuGs8hPlkEYUuNh3WYbxP0X0MAFMjAczFC9YX2yNWMiUA6saBeRODWLF0bknqE3lkXxQP7omAAri0Olid5wLB7cKONw6z8TymhgOt3+8aD4JS4EoXV/iLKck4MDkKxoFhP9Zzlb5f7bKQ0ZhKWCnmc8FhIy3vYpC4vJaH005wYNiPu+SQ3Scrg5HgFwhuN3a0caCUYi6ex8HRdpcw6xie37B+hc86jPdENxuHgyPSua/12XtYzUhegZrnYLMRDAfciOcGz3O4vJrD1LCU5J8Me+BzYOA0qwSC24VtMw6EkGOEkBM696cIIacJIc8rbjsuH/fsdq1LSSJfRbZcb5WbAsAe+WqfaQ9ZYSFZQsjjQNjn3HT7AdlDmUv0N++wka/A67TD73ao3h/zu5AqVG/yqoy5tJbD4XEpj0MIwYTfhmuJ/ofpBILbkW0zDpTSkwYPeZpS+gil9DlAMgyK49KEkGPbtTbGbFzapJXGweO0YyLswXyyO89hT0dICZByEISg73mHVLGGaIfhUjIUcGFjwIxDudbAYqqEQ4q/1YiPYCElpD4Egu1A/dLx5hAhhExRSplexaMAXpJ/ngNwBMAmA0MIeQbAMwAwNjaGmZkZS0+cz+cxMzOD1xelOvm1q+cws9y2kyFbFefmVjAzY00o79JSEbsDNtX1Rd0E739yDTPOZc11bTdXF8pwNKnmc9XyZSylm637b9a69FgtSE15+bXrmJlZAgCEHXW8t9rAqz97DXYb6efyNjEI75cag7ouYHDXtpPX1U/jEAOQJIS8QCn9GoBIx/1DnQdQSl8E8CIAHD16lE5PT1t64pmZGUxPT+PMicsg56/g135lepPG0I8SZ/HqxXVYOT+lFKmTP8Y/P7IX09P3bLn/0MW3USfA9PQTmuvabv78wi+wJ2zH9PTjqvfPZM/j49OLrbXcrHXp8fMrceDn7+GLTxzB41PSR+P1xRNoLlRx+KFPqXpq/WIQ3i81BnVdwOCubSevq28JaUrpi5TSNKQQ0nEAaUgG46axnC5hLOjZIj63K+pFIl9BpW6+ySpbqqNSb6pKU7BzL6ZKltbbK9LFGqJy6a4aQ34X8pW6pde/XSynpfdsl0JFdsQr/d2EiqxA0Hv6YhwIIc+wHAOADfn7KbS9hykAmsnsXrGcLmEiol3rv26h1n9NFq0b1TAOu6NerGbLqDf6p12UKlZ1jUMsIN2XKgyOPMVSqgQbwaau7hGvFEoS8ycEgt6zndVKxwEcVRgBKKqXXoYi6UwpfYVS+gqAKcVtRgntrlnJlDfNM2CwEs+VjPla/1YPQdCtev+uiBeNJu1bH0GzSZEpGSSk/ZJx2CgMTjnrYloSClR6eVGPZBwGsWFPILjV2bacg7zZv9Jx21Py9zTayeaTivu/vl3rUVkfltIlPHXP2Jb7mJQ16yQ2A9uotMJKu+Xeh8VUqfXzzSRbrqFJ0eoIV4N5FckBqlhaSpU2hZQAwGEjiPqcAy8xLhDciuzYJriNgiRLPanSJcxCF6tdeA6jIQ3PISptcEt9yjuwDT/q1y9lVT52EFjOlFrvnZLRoAfrA9iwJxDc6uxY48ASnGphpaDHCb/LbimstJ4tI+hxwOdSd8om5RxHv5LSqaKUR9DzHGJ+ybANinGglGI9W1H1xkZDbmEcBIJtYAcbB2njVzMOABuXacVzUN/EGG6HHaNBN5bS/Umipouy56BjHMJeJ2xkcIyDVDnVxHBg65pHgm7EB1AHSiC41dmxxmGVKZOqhJUAYCLstZaQzpVbMxG02N3HclbmOeglpO02goivN13SlHY/rY3pPA0Htr6vo0EP4vlKT55HIBC02bHGIZGvwm4jiGlcQY+G3JZmGqxnKxgLansOgOStsLDWzYZ5DnphJUAyHplid6Ws//sPP8GD//GneP1yvKvzJPLSmkdUKsBGg27UGrRl9AQCQW/YscYhnqtgyO+CTUN2YTjgRqJQNXVFSinFeq6s2ePA2BXxYjlTRrN58692U0XJKIY8+oVqYa8TmZL1Dffqeg4vvjGHbLmOP/rhJ5bPAwCJvI7nIHtpvahYSher+NOfXsLp+WTX5xIIbnV2rnHIV1Q3G8ZwwIVqvYmcidkLqWINtQY1DCtNRryo1pt9EbdjonuE6GsRhb1OpEvW1/ePZ1dgI8Dvfv4QLq7mupqAp2scgtYbFjv5Tz+4gL/42VX81ndOIVcWnohgZ7NjjUMiX1ENUzDYRpQwUQmjt4kpYUlwK30U3ZIuVg1DSkD3nsN715K4eyKE44/sBgCcum79ajyRq8BGJCnxTnpVdpst1/CDs8t4cHcY2XIdPzq32tX5BDuXcq2Bl08t4PotLie/Y41DPGfkOUj3mbm635Bj40Mqm5gSVs7aj7xDslDVTUYzIj6X5ZxDvdHEhwtpHN0Xxb4hH2J+F07PpyydCwDi+Spifreq8mqsRw17p64lUWtQPPerd2Ei7MEbV7rLkwh2Ls++chbPfu8snn7h7a7zdv1kRxoHSum2eA4pViZqYBxYp+9S+uaXYKaLNS7PIeR1Iluuo2EhL3ItUUCx2sBDeyMghODhPRGcXbQmfw4wQ66+5pBcdsvee6u8M7cBl8OGI3ujeHR/DKeuJ0UFlMA0c/E8fnB2GZ8+NIR4roKX3r/R7yVZZkcah0INqDWogXGQNiMWKuKBXb2qhT+UhL1O+Fz2vngOkuiesecQ9kqPsRJ7Z0OU7hiVprbdMRbEtUTBstigniFnZbfdeg7nljK4dzIEj9OOo/ujWMtWsGyhlFmws/nRx6ugFPizrzyEB/dE8E+3cHhyRxqHbFW6ItS6GgWkDZ6QdhklDy1pCoMrc0JIX8pZKaVyQtrYc4jIxsFK3mFWnnTH5nEfHPGj1qCW1VMT+QpGdEKAUZ8T6S7d96vreRyWjdndEyEA0sxqgcAMb15J4O6JEEZDHkwfHsG5xfQtG1rakcYhU5GMg57n4LDbEPW5THsOQbcDLofx29oP41CqNVCtN7kT0gAsbbqz63lMhD2tGdWHRqXRnrMWx6MmC1Vdbyzm785zSBaqSOSruGNMWiczEpfXhHEQ8FOuNXB6PoXP3jEMAPj0oWE0KfBeF8UY/WRnGweDqqLhgDnjkCpWDfMNjF0Rj+mcQ75Sx9V16xsWT3c0I+zrxnPIb5rLPTUs/WyleqPWaKJYbbSMlRpRn6urnAMrs2VGLOxzYjToxuU16+W3gp3HJytZVBtNHNkbBQDcOxkCIcD55UyfV2aNnWkcqsaeAyAlpTdMhpWM8g2MibA0ba5c45u2li5W8St/9gaOfeMN/NXP54wPUCFV4EuYA92FlW4ki9g71JYjD3kdCLgdWLLgKeXKdfkc2sahW8+BGYdNBm3Ej+sbt3YpouDmcmElC0AyCgDgdztwYNiP88vZfi7LMjvTOFQonHaiezUKAEMBt+mwEq9xYL0OvLLg/9fPrmIlU8KdY0F848RlZC0kitMtz4E/rGTWOJSqDaSKtU2zFwgh2BWxpifFnj/k1e7ojsieg9XqoqV0EXYbac3xAIA9UZ8YPyowxYXlLIIeB3YrpOXvnQzjgjAOtw7ZKsVwwG3YJSyFlfivSFMF/fGbSsz0OtQaTXzvzCK+dP8Enj/+AIrVBn78sfkqiFapLUdYKWTROLDGvokOQUNJbND8ZpuVn1/PkMf8TtQaFHkT3exKVtJljIc8cCimzO2J+bCe4/fsBIJPVrK4eyK0aV+5eyKIpXTJ0sVcv9mRxiFToYZdzIAUVspX6twbRLJYRUxniI6Sdq+DsXF4e3YDqWINv/bQLjy4O4yxkNuSmF2KU3QPADxOOzxOm2njwKTQJ8KbpdB3Rb2Wwkotz8Gjn3MArCXPAelvMBnZaszYfQIBD3OJAg6PBTbdNiVX7M0nbj0vdEcah2xVv8eBwUJEPMnOUrWBcq3ZGpRjBJMKX+ZISr81uwGnneDJQ0MghOCzd4zgF1cTpsMoqQIb9MNnwMJe88qsy7Ln0DnSc1fEi1y5bvoKij1eL+fQ7VjT5Uxpy1yPPTEpZyJCSwIe0sUq0sUa9g/5N92+XzYO127B/NWONA6S52B89Wxm09koSLkJXs/B7bBjJOjm0ld6e24DD+6OtKbLHdkbRbpYw0LS3FVtqiiV2jrtfH92K+J7K7KxGwtvNpItPSmTFVrZUr21Fi1YZZUV173RpFjNlLcaB3m+90Kf5m4Ibi2ub0gXEfs6jMO+GPMchHEYeJpNatpz4AlXsKty3pwDIG2YRmGLXLmGj5cyeOLgUOu2+3ZJ1RDnlsyVyKWLVUQ4jRcARLwuC2GlEoYDbrgd9k23j8rvd9zkSE+esBK7z0plVSJfQa1BtxiHkaCk5bTaB3FEwa3HvOwZ7FdU6QGA12XHeMgjPAclhJBjhJATGvdFCCHH5a/nFbenCCGnlbf1mlSxiiY17nEA2olbHs8hKYeehjg8EsauiMcwIX1uMYNGk+Lo/ljrtjvHg3DaiWnjwNsdzQh5nciUzCV5V7LlLfF7AK0ZF2bnLmTLNbjsNnic2h9V5lVkTa4VaBcE7OpYs91GMBJw90QKXHD7cz1RBCHtcKSS/cM+zG/ceuHJbTMOlNKTOnd/BUCMUvoKABBCnpFvf5pS+gil9LntWlecyWpzeA5REzmHpBxWMuU5hL1YTpd1cwesRvo+uXYakEJSh0aD+GTFXIkcr1w3I+RxmNZWWs+WWzMWlIxY9ByypRpCXoduZZnVslsArTnhanO/R0NurJlcr2BnMr9RwETIA4/TvuW+/UP+lmdxK6E/DmyboJS+qPh1CsAL8s8RQsgUpVS1y0s2Is8AwNjYGGZmZkw/9/mEVHm0dPUTzCQv6z6WKZKeOX8ZeyvXdR/73nVpY7rwwSnccOmXyDKKiRpKtQb+6cQMAi6CfD6/5TX97KMyYh6Cc++/ven2IC3jwkLO1HuwvFGEr2HjPiazUUEyV0c+T7mPWU4WMeooqT7ebQfOXLiKGbrAveYr82U4mk3V87H3i1IKOwHOXZrFDPjPDQBv3ZD+blfOnkb88uZrJXu1jGsZ/tfeua5BY1DXBQzu2njXdfZaCWE7VB9bSVWRyNfw01dfg8vOtzf0al3d0BfjwCCETAFIKoxBDECSEPICpfRrnY+XjcqLAHD06FE6PT1t+jlTHywC73+EY5/91KaOWC1Cb/wEkdFdmJ6+V/dx7//kEuyXZ/GlY9Oao0c7KX+8ir+5eBr77z2C+3aFMTMzg87X9J/PvI4jB3yYnn500+1nqpfw/mtX8cRnPrslvq/5fDM/wZ0Hdhu+ltZrqlzCawtX4ff7t6xLjUaTIv+TH+KBO/ZjevrOLfePn3oN7kgE09MPcz0/APz13HsYd9YwPf3pLfcp36/oL04gMjqO6en7uc8NAB+evAxcuIIvPzW9JVF/InUOP/p4leu1a61rkBjUdQGDuzbedf3bN0/ii3eNYnr6gS33xQML+PurZ3H4wcda1Us3a13d0O+E9HGlEaCUvkgpTQNIE0KOb8cTJnLaw+rV4JVmSMpS2LyGATBuhCtVG5iL53HvZHjLfVMjATQpf6llrdFErlw3FfYKehxoUqDM2QeWlvM5WpVgo0G36ZxDplTTLWNlhDzWJtcl8hVEfU7VCq6xkAfJQhXVujWpccHOoFpvIpGvYEIl1wa0K/WWb7Hihr4ZB0LIcUrp1+WfjxFCnlEYhI3tet54vgKHDQi6+ZymqJ9P1C2Z5++OZrQ+NBrG4ZPVLJq0rdWihMlhz3EqnbakM0xUKwXlKqBSna+fgnWTa+VzRoJu0zmHXKmGkMf4bxXyOlvd1GbYyFcxpFGc0KqwMiGhIth5sLzVZEfjJ4OpBfBK5QwK21mtdBzAUaUHwKqXCCHHADwvVyadlu9+GZLHcAwAWLK618RzFYRdxFA6gxHjHCQjdUebMw5DfhdcDpvmUJnzcjXSvbu2eg4HRuTmGs766bSJ7mhGUN6Uefdcoxnao0EP1s0mpMs1Qw0swLpxSOS1p8yxJDX75xcI1FiR/3/Hw+qeA1MLWLnFjMO25Rzkzf2Vjtuekr+fBHBQ5bCTHd97zr//0t046ufXV4/4XLjIMfQlVai2JJ95YYJ0Wr0O55eziPqcmFT50IU8TgwHXNzKoWbkuhnMOBS5PQdmHNQ325GgG7myJEeiVtXRCaWUO6wU9jotdTNv5Ku4W8UzA6RqJUCqwBIItNDSE2N4XXZEfc6+TH7shn7nHG46I0E3dgX4X3bM7+TzHAr8sxyUTOr0OpxfzuLeybCmlyMZFr6Nqy26Z8ZzMBdWYiEjLc9hyG9O5qJca6LWoLoNcIyQx2Ep5xDXmTLXmiNuQnxRsPNgHsFERD2sBEjeQ7eeQ73RNJ2z64YdZxzMEvW7UKo1UKpqZ2WbTYpUsdra/Mwg9TpsNQ61RhOX1nKq+YbWsREvljiVTtthJX7PIdTyHPgev1Go6kqhR00aByaHwRNWCsthJTN6U5V6A7lyXfPv1q1mk2BnsJopI+iWZpZooXcRyEOjSfHVF9/BY3/4Kr77vrlybasI42BAzGfcCJct19Ck5q7KGZMRL9ZzFdQamyti5uIFVOtN3KNjHHZFjJvoGCkTsxwYLc+hxhlWylUw5NeWQjcjZAjwzXJghLxO1JsURR0j3gkb5KSVkHY5bAh6HMI4CHRZyZQ0K5UY3XoOPzy3gtPzKbgcNvzxjy6i3rQ2u8QMwjgYEOG4emT3mU1IA9IGT+nWSoYLK1Iy+p4Jfc+hVGvwaT8Vq3DZbfC5+HoiAEVC2kTOYTio/R6YvRLPcugqMax0STPjoCfCOOR3YUMYB4EOK5kyxjUqlRhjITcypRoqdWvzQX7w0TLGQx58818ewUahio8T2z9nRBgHA3jE97oxDpMacx0uLGfhdthaJatmjlUjXagh6ndyV2kBgM9lh91GTIWV9CTLzeYcMhyDfhjMgJhRZk3IkidangPA+lxEKatAm5VMGRMq8itKrMrHAFKI+Y0rcfzyvWP43OER/L+/8zgeGOG/yLOKMA4GMAnupE4opBvjsFcW6rreUZJ6fjmLu8aDm6aTdWJmII3UpGdufYQQBNwObs8hXazpVkOFvE7YSHuWtRE8sxza55a8HDPzJ1Icf7eY39wcccHOwqgBjtGNcbi4kkO51sTR/TE47TY8cXAINhMXeVYRxsEAtqHqbWitSiALxmF31Aufy45La+1yWUopLqxkdfMNgMJz4Jg5IInu8SejGUGPg7uUNVOqIaKzkdttBBGfS9fQKuGZ5dBep/SYQpVfmTXNUd47xNkhL9iZJPIVUKou3KhkJCDdb8U4fLiQAgA8vCdifoFdIIyDAWxj0s85SJtMzEJC2mYjuGMsiEuKXorlTBnpYg136+QbAGlT8zrtXFUQZuW6GUGPk6sJrtmkXA1rUZ+zNfvCCBZWCnJ0SLNKkVzZhHFonV9nPnVA6pA3O3VPsDMwavxkjHTRbf/hQgbDAVcrUnCzEMbBAIfdJk1E0w0rVeB12uE1kexVcudYAJcVnsOZeXalENU9jhCCiYiHqwrCrFw3I+jhCyvlynVQCoQNniPmd7Wm5hmRLdXgc9m5JtcxA5Kv8BuHrCzNYdfRwxryu1BrUGRNGB3BzoF5AkZabUMBFwix5jlcXsvh7omQqXxhLxDGgYOY34WkbkK6ZinfwDg8FkQiX0W2Im3Cp+dT8DrtuGsiaHjsWNBj2BhDKTXMB2gR8ji4EtJsnKheWAmQ3kszngNPSAloew55M54Dh8GMmUyiC3YWRqoADKfdhpjPZdo4UEoxF89zKUj3GmEcOIj4nIY5BzOCdp2w3MJcRipPOz2fwkN7Ilx3HeyuAAAgAElEQVRXzGMhN9YMppXlKnXUm9R6WInDc2Dxe6PNXDK0/AlpnjJWQKqsIsSc55DmMD5t4yAqlgRbaYlNckyWtCI8uZatoFBt4OBIb6S+zSCMAwdG4ntGJZxGHNkbhctuw8VkA+u5Mj5e3jwzWo/RkAdrWf1GuLR8pW41Ic1jHFh+wOg5oj4XUgW+GH62VOdqgAPalVVmcg6ZUs1wvUPy31VULAnUiOcqCHocXFphI0G36ZzDbDwPAMJzGFSifpduziFVqCJmYeNleJx2PLw3grOJBk5eWAelwFP3jHEdOxp0o1Jv6s5PtqKrxAh6HCjWYLiZpzl7EmJ+F+pNvhi+mbASIMmwm/EcMkUOzyEgwkoCbfS0uToZCZj3HFrGwaSoZy8QxoGDmNwlq7VBpiyK7in5Fw9NYjlP8b98/xzuGg/irnHjfAOgkJXWyTskuyi1DXmcoAAKBrIUrYY1AyPZ6mTm6EcwE1YCgIDHYS7nwOE5sBxK2oKo33aSKdVwfjnT72XseBK5CldICWiHlcxUvs3FC/C77K3ZIjcTYRw4iPpcqNSbqro91XoTuYq2eBsvv3FkN/aFbHDYCH7/S3dzVyYw47Cuk3dItzwHK2El6ZicQedxRn4OoytxlgDmkbnIcsp1MwImPAcmB260XqlailhSfN0u8pU6vvznP8eX//xN/PWb1/q9nB1NPF/hnio5wrx8Excwi6ki9sR8N71SCRDGgQs92YduGuCUeJx2/MHjHpz+g6fwS4dHuI8bk2cO6A2kYdVBVsNKgHH/QLpYg9dpN5xnHW5dieuHaZpNilylbs44eJzIcRqHfKWORpMi4tV/TwghCHtdXPpVN4u/fe8GFlMl7Ip48WcnL6Nc236dHYE6kufA939lpUua/Z37gTAOHLCKFTUBtpayZ5fGAQAcNmIqjAJI09UA/bBSulgFIXwyFJ20jYOB58ARogHaCWujK/FcReqb4BkRygi6Hchzaiu1qqs415wxMGY3kx98tIwHdofx9eMPIFeuY+bSer+XtCOp1BvIluvcYSUrZdFL6RJ23eTmN4YwDhwMBbTLGdu6Sjc/JghIU6aCHoduWCklJ171mr20CLYE7Qw8B87kcctzMLgSbymyblNYyYyon9QEORieQ6pQxUeLGfzKveP41IEYAm4H3rya6PeydiRGM9M7MVsWnS3XkCvXhecwyOiVM7Ju326a4LplTC5n1SJlQXSPEeIMK/FWFvFKa5vZvBlmEtKt0luO80e8zoHJOXy4kAYAPLIvCofdhkf3R/HW7EafV7UzSbDuaE7PgXkYvBLwTDNNeA4DjF45I7utF2Elq0iNcHphJb6Qjxr8CWm+5/A47XA7bC3PQIuWIquZaiW3A4VqAw2OQSjME+CRFAn7BsdzOHMjBRsBHtgdBiAZibl4wfDvI+g9re5oTs+hNc+Es2emZRwG3XMghPw2IeRbhJA/kn9/afuWNVj4XXa4HDZN42C3aY/GvBmMBT26XdLdeA7cCelSlfs94AnTZC14DmytPMqsZjyTiNc1MJ7DR4sZ3Dkegs8lvVbWXX9RIdwouDm0Z6bz/W+xyYLcnkP61vEcnqKU/hvF7ym9BxNCjhFCTujcf1x+zLN6tw0ChBAM+V2qg+YT+SqiPidsFuL5vWI05NGtn+7Gc/C57LAR3oQ03z+JlOA1Mg7SBs/bIQ2Y01dqaUFxvC9hrxP5Sn3LKNd+MLuex51j7YYoptz7yUq2X0vasfAqsioxM1lwKV2Cy2HDcJ/ymWaMAyGE/DqAiPxdF0rpSZ0THVc8Ji0bhC23mVjbtqM1ESxZqFi+Ku8Vo0E3qo1ma050J8mCdc+BEAKvQ99zKNcaKNea5jwHg+qfjJWEtAll1kypBpfDxiV7wAyIUShMi3KNL9RlRLFax1K6tElKYTzkQcTnxIVlYRxuNol8lVs6gzEUcHMnpFcyZUyEPX278OS+LKOUfoUQ8u8AEACxDi/CLI8CYGGpOQBHAAyp3LbJwBBCngHwDACMjY1hZmbG0pPn83nTx5JKGdcLW4+7tlyCDbC8lm7XBQCJVWkz/KefvYk9wc32vtqgKNUayKwtYmbGWsmjx0ZxZX4RMzPqVTHpsnRFvbZwDTMzi4bnqxXKWC1T3dd69koVBMD7b7+pOfWq8/2ai0vvwxtvvYflqP4/7KW5Cjy2Jtf7vbwsnfenM7/ARMD4ekq5rtl0A18/Vcaoz4b/8CkP3A7r/+jzWamfoRSfx8zMUuv2UXcDZ64uYWYmyb2uQWNQ16a3rgtzZfg5P0OMZqmMG0n9zz7j8o0S3FDfW27G+2VoHAghX1D8ehrAGQCUEPIFSunPLD5v50ijIY3bNkEpfRHAiwBw9OhROj09benJZ2ZmYPbY769+gPfnU1uO+0+nZ3DXeBDT049YWku36wKA4HwSf/nh29hz+D5M3zm66b7ldAk48TMcvf8uTD+219K6fL/4EfzhIUxPP6p6/+W1HDDzBh576F5MPzBpeL4frH+E+NyG7mt9LfMxQsvL+MLnP6/5mM73KzifxDdOv4077n3AsJHw71Y+QKyY5nu/L63jhbOncPj+h/HIPv0ZG53r+stvvY1Ko4yFXBOrvgP4V0/uN34+Df7ho2XgrQ/wL6Yfw13j7UFQ/xj/CG9cjhu+Fqufr5vBoK5Nb11/eelt7PUC09NPcJ/vxxtnsXhxneu1/sf3Z3DPZAjT00dMratX8ISVDspfz0G6mj8C4JcBfK2L500DiHHcNjDE/G7NhHQ/y1iBdiOcWq8DW3M3Hdw+h36fg9myU6PhSeycZvINABBwS8/Pk3PIlWu6E+CUsNdlNqy0lC7hvetJPPvP7sQ9EyH84KNlU8d3MrueByHA/qHN8s37h3xYz1VQNDEiVdA9CROiewxpngmfKvF6ttwXTSWG4X8fpfTbgJRgppT+CbudEPLNLp73FNqewhSAE/LvnbcNDEMBF4rVBsq1RivGWG80kS7W+tYAxxjVkdDoRamt10F0cw6tslADKQpGxOdEodpArdHUnFmRLddNV4CxnEOBI+eQr9RbCWwjWKLdKE/SyVtyc9oX7hpFoVLHt16fMy0mqGR+o4DJsHdLjHufbCxuJIubPArB9pLIVTB8yNz/1VDALakSl+q63fmFSh2FaqN14dcPzCSko4SQXyeE7CeE/AakvIEmcoL5KEs0y7edAABK6SsApljSmVJ6Uu02k69lW1GT0GAJ4H72OACA22FH1OdUldDohefgdepXK6U5RfcYPI1w0ghPk8aBzZHmMA65cp1rNjWgUGY12evwzlwSMb8Lh0eD+PShYTSaFKfndYv8dFlOl1XLGpkncT1RtHxugTnKNUk6g1d0j8H2ioRBUnpdLpNl2mn9wIxxeBrt8NIBAF/UezCl9BVKaVTe9NltTyl+/rpsFF7Uu21QaInvKcpZ29IZ/TUOgNQlvZrRDit1Y8B8DqIbUuGV62bwGIdMF8aBL6xU5w4rhSwah/PLGTy4OwybjeC+XVLTWjdVRcuZEibDW68k9w75AAA3kgXL5xaYg10kmiljBfj1lVgU4FbxHB6BlJB+BVJSuvsM7C0E01dSWnwmndFvzwGQeh3UZkmzJj2roQxAMg75Sl0zTpop1UCIJHzHQ5hDfC9bNjfoBwDsNgKfy87VLSzlHPjWa7cRBD0OU41wtUYTs/E87pTDPCGPE/uGfPh4ydoMhkaTYjVTxqRKt2zY60TE58T8hvAcbhaJnPkeB6C9jxhNFmSew2gfPQczGT+lMTgIIArAarXSLQfLKyg9h1aHZB+TRozxkBuXVrdelSaL3TfpeZ1Ak0oDf9Ti9ExXifc5eAb+WElIA4BfltDQg1KKfIU/rATwNe4pmYsXUGtQ3D3RHtp0z0TIcrNaIl9BvUkxoSGlMBH2YjWjLaEi0KbRpKZFKdn/vvmwkryPGHgO6y3P4RYwDpTS/0P5O5PR2Cm0cw5tzyHeigv2z/VjjMld0p0f9FQXDXAMn1ybnyvXVI1DuljjErBjRAzCSpW6uaY6JX6X3bBqp1BtoElhzjh49UfFdnJRNtR3Kib6TY348dMLa7qJeC1aUgoR9c/aRNiDFWEcTPP9D5bw7PfO4ompIXz7fzgKl4Pv72JWV4kR9Uuf6Q2DWdLxXAUuh62vsjxmtJW+RQj5JvsCMFAdzNtNyOOA12nfpGG0li3D47SZmjmwXYyGPGjSrR+6jR6U2npbxkF90+WV62a0ZbvVN1v2PFbmT/jdDsNqJZaTYKWvPIS8DlMTvObiBRACHBhul50eGA6g0aRYlAXVzLCSljb+ibCW5+DBqo74Yj84t5jBfzl5RTXcaYX5jQK+9fqs1LvTAzLFGv7g//sYYa8Tr1+O47++O899LDMOZkPKbocdQbexvtJ6roLRoLsvE+AYZi5fXoDUgPYigBcppbrVSrcbhBDpH1BxdbaWrWAs5OnrH5AxJl/BdG4QqZ4YB+m7Viw/U6ohbMI7aSek1TfblnSGhTyJ3+VAoaIfVmKvw4znEPI4TfU5LKSKmAh5Nk3GOzAsJY6vJ8wnjtmGqJZzACTjkCxUB2Yq3HK6hK+88Db+7ORl/Ou/PtW1fEi2XMNvfPNt/PGPLuJf/tW7PXmd/3B2GblyHd/514/ikX1R/D/vzHPPd47nKqalMxhDARdXQrqfISXAnHGYpZR+wL4IIfu3aU0Dy0TEg5VM+6plLVvGWB+rCZSw0FanOmsvmvRYWEnryjlT5FdkBQCH3YaA26HZN2BFkZXhcxuHlVipq1njYKRMq2QhWcTumG/TbQeGJU2kOSvGIVOC32XX9FLHZY9CT7r9ZvKt12dRbzbx7D+7ExdWsvjxx6tdne87b15HIl/B7z11GNcSBfz9B0vGBxlw4sIaDgz7ce9kCP/tw7swGy/g0hqfum0iXzWdb2BIOm08nkN/9xYzxuF5g99ve8ZDm5N+67lKX6sJlLSNQ3t9jSZFqtgDz8GpH1bKlMzlHABp49fKObRF9ywkpF3GCWn2OswYh6DH0ZoxwcNCsoQ90c3GIepzIuhxYH7DvHFYzZQxHtb2UifkEtdByDs0mhT/dHYFv3zvOP7N5w5iPOTB9z+0vplTSvH9D5fw6UND+N0vHMLBET/+4cPuus2L1Tremd3AF+8aBSEEv3zPGADg55f5purF8xXTlUqMmN/dCktpsZ4t931vMTQOhJADhJCXAXyVEPITQshPCSE/hVSttKOYCHuwJid9KaWS5zAAyWhA0pS3kXaVAyAlz5u0+4oHn05Yqdmk3POjlYS92mEa5qFYCSv5XHYUDXIO7bCSmZyDE0W5q9uIaoNiNVvG3g7PgRCCXREvltPmN/C4wZXkuGwcBqFi6YMbKWwUqvjV+8ZhsxH86v3jeP1S3HIo6Mp6HtcSBXz5/kkQQvDl+yfw7rUN3Wo3Iz5eyqLaaOKJg5KE22jIgwPDfrx7TV+8kGFFOoMxZOA5sAa7gQ8rUUqvUUq/AuCPKKW/Qin9ZfZ1E9Y3UIyHPWg0KRL5CrKlOorVRl87GJU47DYMB9ybwkpMa2m0SwOml5DOVepoUvMhID3PoZuwEk8pazshbSasxDf0CAA2SlLcek9sa35Aqioyn1BN5Cu6lTHj8t942cK5e82p61IX+JMHhwEAnzk0jGqjiQ9upC2d7905aQzqZ++QzvfEwWE0KXD6Bt9GrsaHC9IaH9zT1vt8bH8Mp64n0eTIj8RzFcthpaGAC6mitr5SPNeb/9tu4fEcWMnqECHkj5Rf27y2gYO57svpEm4kpYajvTG/3iE3lbHQ5ooVFmLq1rtx26VGMDXPwepGrjcNzsosB4bfbUdBp2EPsBpW4huXCgDxkuRd7OnwHABgIuK1FPpJ5Ku6E8f8bgdCHkerqqmfnJ5PYmrE3wpnHt0fAyHAu9eszbp+73oKYyE3dsvSIQ/ticBhIy0jZIWPFjLYHfVuCg09si+KTKmG6wZhv3KtgVy5zj0BrpOY34Vag2rm8NYGoMcB4OtzeFn+vmPGgmrBygiX02VQSJvPvqGtG0C/GAu5N5VJ9kqfhRCCgNuhetXMNnizxkGvqSxbrsFlt8HNWXOuxOdyoN6kqDaamyqFlOTKUke332XCc2gpsxp7Dsmy9NlQqyyaVFQV8Va6lKoN5Ct1wxg363XpJ5RK+lHH7h5r3Rb2OnH3eAjvW9jMKaU4dS2JR/fHWvkWr8uO+3aFcboL43B+OYP7ZUkTBhu5emEliynFQKVOrEpnMNpd0hXV/5tWd/SgJ6QppR8ovkc7vnYU++VSxLl4viVV0BlX7idjoc2NUGvZMgix/iFWEvKqGwe2wfOOCGVI0+C0wkp1hLxOSyXCfpe04RZ1yllzlToCLoeprnEWVuJJSmcqknFQi0mzCwwz3gNLXhrFuIcDxonO7WYtW0GqWMP9uzdvvA/sDuPCSpa7VJSxnqtgNVvG0Y45GvfvCuMTC+cDpCbLG8ki7hjdbAAOjwXhtBOcN9C/iluUzmDEDLqkW93Rg56QZhBCTgF4CpKMxiOQ5jrsKHwuB3ZHvbi8nsf8RgHDATf8JuLW283emA+ZUq21Ya9lKxjyu0x346oRdDtVQypmZjErCfucqNabqknKrEXpDADwyX+Pgk45qxlFVoaZsFKqQhHzu1S7bSfkDucVE41c8TyfVMNwsP/G4bJcCnrHaHDT7fdMhpAsVLeUWhvB5EbYrGzGneNB5Cr1Vue4GeY3imhS4GCHcXA5bDg0GjQUR0x0KZszpKLwrGQ9V4HDRhDr8/hhM/8hr1JKf3/bVnKLcHgsiCtrOdgI2aSbMwiwENdCsojwrrA8LKQ3rmnQ41ANqZgd9MNQKrN2hle6mXnAQkVFnaR03oQiK4MZK56wUrpMNePFkyw0acZz4LxSHQ64+h5WYsbh8NjmjfeeCRayybQqq3i4tCqdr3NOBfvfu7Saw+6oOe/96noeADbN4mbcOxnCzKW47vEJTmOthZH43rqc7O7X7GiGmUvKI3Ipq1JCY8dxz0QIF1dzuLCSxQMdrnO/YQlQlixfTJUwqaHFY5agx6kaUrGac2hLaGw9Z8akHIcSn1syNHmdctZcpdYaDMRLK+fAGVbSKgJol5ya9xyGg/pXksMBNwrVBkoG1VrbyeW1HIb8Lgx1GLK7mHEwKVl+cTWH8ZBnixz84bFg636zzMrGYWpkazHJ4bEAEvmKro4WM8BW1ZiZ+J6Wl8ekM/qNGePwHID/GQoJjW1Z0YAzfWd7NvGn5VK9QUFpHCilmE8WWlPCuiXk0c45uB020zICbGqcWlJaCitZMw6sPFU352AhrBRwOUCI/rhURqqi7Tl4nHYEPQ4kDCSblSRybCaH/obBchL9DC1dXsu3Nm4lAbcDe2M+fGJyM7+4mtskXsgIepwYD3kwG8+bXuNsPI9dES98KgUJzJuYjWtXLCXy1qUzALQE9TSNQ7aMkQFQXjA1z0EpnwFgTvYgHtquxQ0iR/ZGcfyR3fj1h3fh8amhfi9nEyGPE1FZ1389V0G51uxZNVXQ41CNt2eK5hvgAH3xPWlEqMWcg5yQ1ss55Mv8I0IZNptUsWWkr9RoUl3PAZA2cTPhn0S+gojPaagYysIc8T4ah7l4HgdH1S9IDo74Maez6XZSazQxu57HXRrh2/3DPkszLGbjBVWvQVojMw7aRieRr1pugGMMB1z6nsMA9E+ZMQ5HCSEvyT0OIbS9iK9tz9IGE5uN4E+efhDf+OpDfY8JqnHHaBCX13Ktf5peeQ5Bj1N14E+6VOWeHa1EaxocpdTSFDhGO+egYxxMznJghDRCa0o28hVQ6JcPDwfdpjbwBKdUA3tMok95h0yphmy5rlnBNzUSwLVEnqvJDJByZ9VGE4dH1Y3DgWG/JRHDG8lia7RqJ7ujXrjsNl3j0I10BmM44G55hEqq9SaSheotF1aKUkq/Cqnv4WsAjsgehLXRVoJt4Z7JEC4sZ1uDf6aGe2UcHK2BP0qs5ge0psEVqw00mtRyWInlHPSUWYvVhmpIwYigRmhNyTpHd+uIyZLTeK7C1XDFchL98hwWkvrl3VMjfpRrTaxwigOyC5z9Gp/hfUN+bBSqpjSvcmWpmm+3yixuQFIa2D/sw+y6Tlipi+5ohlZlGbut3z0OgDnjQAghvw3gGQBDAKZkZdaI3kGCm8t9u8Io1Rr43pklxPwuzX8Cs2iVcqaLNe7Z0ZvO55Zi+J3GwWr1E8PIc6CUolCtt/ohzBDS0YNi8HS3jgTNhZU2CtUtCV41WolOlSvSmwEzDlrVQ1OyKi1LCBvBOpX3a4RG2dX/fII/tNQamqTzf3FwJIA5Q8+huzLTkYC699irxtVewG0cZH2lFKRQ0ksAvgrg62h3UAsGgE8diAEAPlxI48jeSM9mTQQ1tIWseg42ea51p3FgV4FWw0peJ6tWUvccyrUmKG33Q5hBCivpew6sjl8v5zAccCFXrnML0SULVa6ad6NE53azkJI9B43N/KAc59fbeJXMbxQRdDs0VYVZU6qR3IWSxaRkHPTKXw+OBDCfLKJa3yqy2JbO6G7zHvKrfwba40FvLc8BlNLvKZLSZyilX6GUqs6RJoQcJ4QcI4Q8q3LfEULILCHktPz1vHx7Svm7wDx7Yj48PiUZiOOP7OnZeVmYR81zMCvXzVCT0GB9BFab4Gw2Io0K1ShlZYlqa56DelJeCZt6prd5DJuoKmo0KbLlGqKc3tlIHxvhbiSLCHudmoZ9JOhGwO3gnmdxfaOAfcM+zQucfbKuGSvd5mFRNmC7NIYmAcDBUT8aTYobya3rtDo7uhPWQNfZCNcOS/bfc+D+DySE/A6kclYKKc9AtabBEUKOQ3rASULIFCHkGKX0pOIhMUrpQfmxRwAwucanOx4nsMBf/atHcWUth4f39k7hJNiSj2hvuuVaA6VaA1GL9d5q4nvdhpUAySvQUmZlJa5Wcg480+A28lX4ndCtLGIbSyJfNWzgypRqoJRfnqSfjXALyZKunAwhREoic1YYzW8UW3pHanhddsT8LlNjQ5fSJbgdNt2wEKtYurqeR+f1OxO2NNPIpwa7QNjIVzYZqvVcBYRY76HoJWY8h2OU0kOQQklfBPCqzmMfBTAn/zyHDqmNDgMwRSllj40QQqZMrEmgQsDt6KlhANQlq9u6StY2cjXZbrb5Wg0rAZJXoJVzaHkObgueg8chSZTrVNski1UEnfqhPLYx8GziKbnUlw2mN2Io4DacMrZdLCSLqjLlSvbGfK3chB71RhMLyaJmvoExGfGYMg6LqRJ2R7264dYpnV4HNi+je+Mgbf6dXl48V8aQ3w1HDyRvusXM5ROTQHwfUlL6izqP7UxSqzYEEEKeoZQqm+liAJKEkBcopVtKZAkhz8jPjbGxMczMzHAufTP5fN7ysdvJIK/r3JlTAIDTH51HKHUZALCQk2KyS9euYKZ0zfR5K7kyVrLNTa/59HXJOJw78x6uu/Q3Wa33q1kt48bymup9V1KS53D14nnMJC6ZWu/6knQV/5OfzbRmXHQyt1iCz97U/TtuyJLevzh9Fs51/U2frXfh6kXMZK4arrGUrmA9U1d9/u38fFFKsZAs4nCgovscNF/FjY0afvbaa7ApNujOta0Xm6g3KcrxBczMaI8YddXKuLKU435dn9woIeAiho+PugneOjeLfVO1TY/9xTXp8zl77jRWL1rP58WL0mfgzffPwrba/gxcuFaGj1DD9d2MvcKMcXgekNRZCSFHIfU5aJGGtNEb8RQUndbMUBBC0oSQ45TSV5QPlu9/EQCOHj1Kp6enTSy/zczMDKweu50M8roee/IzwMxPMLFvCtO/dBAA8M7cBvCLd/CZow/hyUPmu8VPpM7h6serm17zmROXgYtX8KVj07Ab9JFovV9jF9+C027D9PTjW+6zXY4D776HJx49gkf28XxE26z5b+BvL53DA0cf14xZ//GHbyDsKOr+HSv1Bn7v9R9jaHI/pqfv0H3O+oU14N338bnHj+KhPcaFgWdql/HawhV89nO/tOX9287PV7pYRe0nJ/DofYcx/ZkDmo9b9t7AD6+dw50Pb34PO9f2xuU48MZ7+JVPP4LHDmj/nWay5/G904vcryv78xN48uA4pqfv133cPVffQaHSQCBQ23TuN/MX4Jmbx5eOTXdV7FGuNfDv3vgxhnYdwPT0odbtf3ruTUzFXJiefkz3+JuxV5ipVroGAHID3EsATuk8/BTa3sMUgBOdDyCERDp+f4blKgBYmwoi2Da8TjvsNrIp5s66m62UsgLthLSysS5TrCLkcRgaBj38bgcKGglpFm6ymnMAoJt3SBaqCBp4PG6HHUG3A0kd/R5GK6zE+R7HfE5Qqi5Lsp20YvEGg6VYTuKGQd5h3qCMlbEr4kWuUufqdShVG0gWqrrJaMbBkQBm4/ktTZ+r2TLGQ9qzvHnxOO0IuB1bwkpr2TLGBqBSCTAn2f0yIeQnAP5K/vq21mPlK/4pQsgx+feT8jmURiIGQDnn72UAacUxm7wGQX8hhGxpAkvJyeSoRWnhsNeJRpNuEsnLlKz1TSjxu7QT0qw5zsygH0a7Yku7hyJVrCJgkHMAgIjfiRRHboAl7HkT0qw44GbnHdqxeP0qG2YcjPIO1zeK8DrthlVBrF9hKWWcd1jjNGCAZBxy5Toy1c3GYS1b7jrfwJAkNNp/p0aTYqNQHYhKJcBcWCkp9zpwQSn9usptTyl+noNCeoNSmgbAEtWiYmkA6dRXam9c1hPSgGQQWJNdulSzJMehxKdTytryHCwkpFsVWxpX5blKHbUGNfQcACDmcyGpMSZVSapYhd1GWgUBhueVjUOKwyvpJcw4GI2knYh4YLcRw/LT+Y0C9g1pl7Ey2LS95XRpy8yHLWs0MTaXVSyt5Dcbh5XM1sFDVhkNeloGC5AKFBpN2jPj0y1mjMNpQsi/RbsKCZTSv+v9kgSDSmd1USFKGQkAACAASURBVLpYhcthazWemT9fW5l1d5Sd05qQnxK/Tikru92S58DCShohDOYJGChrA5A8AZ4NPCX3kfCGMZgXd9M9B87mLafdhomwh8M4FDXF8ZQwSXqeiqX2THXjK3P23CuFdiNcs0mxnq1grEeb92TEg/fn26NOWfe22njZfmCmXuprAIYBHFR8CXYQUZ+rFUoCpI086rM2zhNQeA6Kc2a7mOXA8OmUshYrdRACeJzmSwWNwkpsQ+YJK8X8Lq4NPF2smjKWLKzEE7LqJWvZMoYD6tPvOtkb87W6qdWglOJGssg1gnfY74bLbsNS2livaT1rrHvFGA954HPZNxmH1WwZ1UazZ6OBJyNerGbKaMil0S1pjwExDmYun05SSvUqlAS3OTG/a9MVX6poTZGVEVER30v3wDj43Q7UGhTVenPLZlWoNuB3OSwZNKOwEtvsQxxhpajPpTroqJNUsWoqp8NkNniS3b1kNVPmCtcAknE4+cma5v3xXAWVOt8mbLMRjIf5eh3WsmV4nDauEJ3NRjA14sdKod3r0FI6jvVGzHIy4kW9SRHPVTa9hlvRcxCT4HY4Ud/mq91uQ0CtmQ7yZsvkursOK7GZDip5h2K13pr5YBanXQqhaYWVWp4Dl3GQJNArdX19Jek95jcOXpcdHqftpnsOq9kKV6IXkCReEvmqZkUZ8yp2c16hj4c8LdkSPdZyFVOVRgdHAljJtz0HJqfRqxkprWS6bBSW0yWEvU7Ts0a2CzEJTsBNTBYLY4Jk6ZK5kEcnnTMd8pU6Gk3afUJa/udSG/iTrzTg7+KfT9JXUt/UWA6BJyHNwj9G3oPkOZh7j2Md4b+bwVq2zB2Lb1UsaYSWbhhIf3cyGnK3QkZGa+QJKTEOjgSwUaatsavzG0U4bAQTPco5sPARMw5LqdLAeA2AuT6HDzq/tnNhgsGjvaFJm2CqWLNcxgpIuQGnnbSMg9V51J20Zbu3XpUXK9Y9B0B7ljYgiai57DZ4OE7P3je9pLRUGlszrV0V9btuqudQqUv9A7yeg1Gvw42NEgjhj72PhTZX/WixnuUPfQFbp8LNJ4vYHfX2TNqCGRkWTrqRLGJPjyT2e0H/BTwEtwzKeDalFOli1bLoHiD1TijF91qie12GlViZal4lbCHNcujCc/A4WsqxnaQKVUT9fAl6ppWkl5Qu1Rqo1pumvbOY33VTcw7rWXMzCPYqZp2rcSNZxHjIwz2jeSzkRqHaUP17MyilWMtWMGZCTfVeWfTv7KI0z+zyaq5lMHpB0ONEyOPAYqqIeqOJ6xsFHBzt3fm7RRgHATeshj6ZryJdrKHWoF3P0o34XC1PpBeKrEDbcyipeQ7VhqUeB0bIq+05JAv8nlSMI6xktckw6ru5ngPr8uWVsY74pE1Ra/6zJODHH9dn3oCe95At11GqNUx5DvuGfAg4gQ8XUijXGpiN51sGo1ccHA3g6noeN5JF1Bq0p8anW4RxEHDTMg7FqukNQQvloHX2vVu5Yp9OQrpQqXeVcwh6nDqlrBUMcU4I4+lHYBu86ZwDZ5lsr9iQu3zZJDojCCHYP+zXHNLDW8bKYL0VesahNUTHRPcxIQQHI3acuZHGxdUcmhS4ZzLMfTwPd40HcXE1h6vydLyDHL0dNwthHATcsFBIqlDt2dCTkaCndS4mJdDtlC1mHEoqk9aK1YalQT8MKayk0QRnIgfDQkVpnfCPWekMRtTnQrZcR62xdZKZFuVaA3924jL+/oNFU88FtI36sInPwt6YT9VzKNcaWM2WscdgzoUSFs7SS0qzCX28eRHGnVEbrq7n8fL7CwDAJX5ohrvGQ0gXazhxYQ12G8HhsWBPz98NwjgIuGlf7dZa82+73chHAu15yhv5Chw20pM+B6Cto6SkUKlbEt1jsLBSpyAbII/z5PR63A47/C47kgW9sBLzHMwmpJnh4a9Y+s//dAH/5dUr+B9f+ggzl9ZNPR+bZmbG49s/5MdiausoTla5s3eIPzE7yhFWWjMhnaHk0XHps/I3797AfbtCPZe2eFA2Nt89vYh7JkJdebW9RhgHATdOu9RAtFGo9NBzkJKJxWodibwUlrF1ocgKtD2Hzi5pSqnkOXSRcwh7nag16BavpNZoIlOqcRsHQK4q0vEcWG7DrLHkqYRSkshX8PKpRTz9yG7sjnrxzZlZU88Xz1UQdDu4E8iAFM9v0rYxYJgtYwWk4VYBt6PlHaixljMfVgKAEZ8Nv35kF2wE+N3PHzI+wCQP7Aq3/oe+ePdoz8/fDYNjpgS3BJMRL5bTJXicdrgcfN2merRGZuaqSOSrXXsiQFuOu9NzqDakATJdeQ6edm+G8jzsKj3mdwGcUzqjBvpKLLdhdp52zKQy66ufrKHaaOK3Pn0Au6M+/J+vXsZGvoIhzr9FIl8xFVICgP3DUmx9fqOAA8PtODtTazWTkAakTX9NpxFuPVtB0OOw9Lf/06cfxB/+2v3wdhGO1MJmI/iL33wYPzm/it/+7GANwRSeg8AUu6M+LKZKWEwVDcct8sDGJcbzZWmT6YFxsNsI3A4birXNnkOxJdfdnecAYEs5q5UQkNqYVCXZUg0OGzEtbMiTz1Dy2sU4JsIe3D0RxBfuGgWlwMylOPfzbeSrposIWJdxZ97hekKW6jb5ORgLelpJZzXWTPY4KCGEbIthYDw+NYT/7Z/fOzCd0QxhHASm2B31YjFVwvxG0VTSUAvmOcRzUqiqF8YBkPIOxQ7PodCS67b+T9jZ1c1oV+z00DiUawh6zOtAsQQ2z8AfSilO30jhiYNDIITg3skQQh7HJrVQI6wY9ZGAGz6XfUvF0lwij6kRv+nXPBZy64aVVrNl7j4MgYQwDgJT7I56ka/UcX452xN1SnY1t5AsYTVbbunNdIvPZd8in1HsQq6boWUcWp6DCeMQ8jo1G+oAyTsJWUjOR7z8CenVbBnxXAUP7pYSozYbwYN7IvhoIc39fBuFKncJL4MQolqxNBvPW6r1Z13SaoUCgBRWGpQJa7cKwjgITKGMDx/qQTfnkN+FgNuBt2YToBQ9kw/wuexbmuBY30N3TXCSYek0Diy+byYhHfJKZbFaG1q2XGvlOMzgc9nhsJGWoKEezAg8sLtdv//g7ggureVUmwg7qTeaSBWt5Yr2D23udSjXGlhMlSwZh9GQB5V6U9XYUkqxnjOnqyQQxkFgEmWd95G93U/EIoRg35APb15NADCfiNTCpzIqdDs9h2TBWs6h2miiXFPvR8iWaqaT0YD0nrL53EZ8vJSF3UY2TVG7f3cYjSbFJ6tZw+OThSoobeeOzDA14seNjWJLmfZaogBKwTXkpxMWMlJLSqfkbn4RVjKHMA4CUwwF3Pja56bw6w/vwn27eiMlcGDYj1pDunq2sjGo4XdvHRXa8hy6FN4Dts50SBaqCLodXMNuGFqGhpEr1y15DuzcGY6w0mw8j30x36YyVNaINSt37erRTePiXRMh1JsUs+uF1loAWA4rAeq9DlZ7HHY6g5UeF9wS/P6X7u7p+R7eG8U/nl2Bz2U3HDPJi9fpQLKwuYa+5Tl0kZC22wiCHodqzsGsCKHSOKg1V1kNKwGyZlXJuFppLl7YYpD3RL1w2glm4+ryFkqsdEcz7pmQjNAnK1kMyd8d8pAds7B8AptlrWStNcJUeA5mEJ6DoO/82kOTuGM0gP/w5Xt6dk6/245SR0KaqXZ2U8oKSL0Oap6DmXwDYOw5SAlpa4bMqBIKABpNimsbBUx1XKk77DbsH/K3ruT12ChY18PaP+SHy2HDRTl8dW4pi8NjQVPNdAzW3KbmOaznmGqs8BzMIIyDoO8MBdw48T/9Ev77T+3t2TnVcw7dl7IC6htvr41Dtd5EqdZohbHMElFIoWuxlCqhWm+qir0dHAlwGYdETg4rWbgqd9htuGcihA9upEEpxbnF9KbEuBk8TjsiPidW1YyDfFu33fw7jW0zDoSQ44SQY4SQZzXuTxFCThNCnuc9RiDgxe9SyzlIxsJsU1knasYhVTA365mdB1A3DjlZOsNqB3rYZ5xzmE1Im3+n5wAAB0elZLGReF+iUIHLbkPQosF94uAQPlxIYzbdRKpYw5F91oscxkMerGa29jqsZSsIe52WPJKdzLYYB0LIcQCglJ4EkCaEHFN52NOU0kcopc+ZOEYg4MLnsqNYa2wqEy1W6/A67bB3qd0U7pjpQCm1VOuvZxyyLekM6wnpXKWOus7mfj0h5RT2D231HA4MB1BvUiymSlvuU5LIVTEccFnulP/MoWHUmxTfOS9t6p+7Y8TSeQBgPOzBanbretdEA5wltish/SiAl+Sf5wAcAXCy4zERQsgUpXSO9xhCyDMAngGAsbExzMzMWFpcPp+3fOx2ItZlDr11rS5KJZY//dkM3HZp47pyvQInaXT9WgrpCtbT7fOU6xSVehPp1QXMzKxxv19N2XCd/eQKZurzm+67lpHnFl+9iJnsVdNrjC9JBudHr77emmndua53L1bgtAEfv//Wls09kZSe/4cz7+DeYe0r7ss3ynBRavk9bVKKES/BUp7igWE7Ln7wDi5aOhPQLFRwI77173t1qQSvA5bWeCt+9nvFdhmHTtHzIZXHxAAkCSEvUEq/xnMMpfRFAC8CwNGjR+n09LSlxc3MzMDqsduJWJc59Na14L6Oly+fxyOferJVZvn91Q8QKaS7fi2/KFzAqfX51nkWkkXg5Gs4ev/dmH50j6n3K/j6TxAd24Xp6Xs33e64kgDefheffvQIHjsQM73G9AdL+K+ffIh7H360FTbqXNfLS6exJ5bD5z+/da0Hk0X88XuvYXjfHZh+VDsX9I2P38S+mAvT04+ZXiPjO4cz+It/eAf/629+jntutBof1C7j50tX8ORnPreppPjfv/0qHto3hOnph0yf81b87PeK7co5pCFt/ppQSl+klKYhhZCO8xwjEPDilRvdlPpKhWqjqx4HRtjrRLnWbDVvWemOZoQ86lVFLGzVTbUSAN0u6aVUSVOuZCLsgd1GDMNKqWLV9KS6Tu7bFcZv3u3uyjAA0popBdYVjXDNJsV6riIqlSywXcbhFNqewBSAE8o7CSHPsBwDgA2eYwQCM7ByVaUya7Ha3YhQRqcya8s4WOgS1io5ZaWylpvgfPplsgCwlC5rbsgOuw3jIY+xcSjUTPd3bBdj4a2NcKliFfUmxZioVDLNthgHSukrAKZYUllOMoMQwjb8l6FIOlNKX9E6RiCwgk9lGlyh0hvPIdSRSLYyCY2haRxkzyFosVqJie9pVSyVaw0k8hVM6lyt74p6saRjHKr1JvKVuukqre2CjQBVViwxpVahq2SebeuQppR+XeW2p+TvabSTzSf1jhEIrOBXmQZXrNYx0YMxj53GIVUwr8jKCHudqv0E2VIdNmJdB6oVVtKY6bAidxLrhXJ2R7x4Z25D837Wgd1tWKlXsL+tsteBaS2JaiXziCY4wW0JG86y1XPoZVip7Tk47cRSrb+W55Ar1xD0OC2PTG2XyapLgjOPQM9z2B31YjVb1ux1SMnzrwclrBT2OuF22LCaaXs7ceY5CLlu0wjjILgtYVfcpS05h94kpIG255AsVBDzW6v1D2uop2bL1qUzAClnEHQ7NPWVluXZzbt1JNJ3Rb1oUnW9IsDa9LvthBAi9zq0w0rMQzI7O1ogjIPgNoXNbChsqVbqnefQNg41xPzWNp+w14lKvYlybbPUR7ZkXXSvdW6dLumWGJ3OpqmndAq0Q1aRAQkrAVLeYU1hzJbSRYwE3XA7RHe0WYRxENyWMCPAcg61RhPVerNr0T1ASvYS0q5SkjwHaxtkyKsuAd6NIitDT3xvo1BF0OPQ3TTbxkF9/GZSDitZKeHdLsbDHqwouqSX0qWuS2R3KsI4CG5LmH4S8xyYXHe3onuAFLKJ+lyIy3LVkuiedc8B2Fpymi3VLVcqMSI+p2afw0ahalhdxYzDusoAHWDwwkqA7DlkKy3ZFL1eDoE+wjgIbkvsNgKv045SjRmH3sh1M0YCbiRkKWiejVYLJqyn1Gpiv1vVVWJEvC7NaqWNfAVDBgN6oj4nnHai6Tmki1V4nLaBErSbjHhRrTcRz1XQbFIsp8vYLTwHS4hhP4LbFr/b3pr+xjyIXngOADAcdCGRr6BUbSBXrltOeGp5Dt1MgWOEvE7NaqVkoYq9BiNZCSEYDXpaktdbz1FDbIC8BgDYL884vyaLClYbTeE5WER4DoLbFq/L3gonFXo06IcxHHAjnq+0R1BaLJUMdXRbA0C9ITWXdVOtBECeI13dpEzLSOT5VGRHQ27VucyA5DlEBsw4TMnG4fpGATeSRQD6FVkCbYTnILht8bscbc+BDfrpQbUSwMJK1VbDldqYTx6Yd6AMK7GJdd16DhGvE7UGRbHa2CQb0mxSpIpVDHHkScaCHs2hP9Jo1MGpVAKksJLLbsNcooCmbBPvGA32d1G3KMJzENy2+FyKnEOFzY/ukecQdKNUa2BOnrNsVdiNeQfKaiXmRXSbc9AS38uUamg0KZfnMBZya5aypoq1gUpGA1Kuae+Q7/9v736e27quO4B/D/GLBCkSIikztdWxh6Q9mrqOpxTdznjahm6piVfdhHL+gUYcLzrTldRssk2pLLsSt+nCtrzPJGRmmHTaTitLTpOMMh1HbN3KkSWTIEQS/AGAvFm8ex8eH0ACeHiPuHj4fmY8pAg84BAG38G9591z8b8bRXz2dBcDqQSvVgqIyYFiazAT7cgBAH79u+cAgrdnyCQT6E/1nag5bLe5C5xh1h/41zq4+z43KEgDTk+i7YMK9n1brgKmI6tdyQEApi8N4TdPdvDZsx1MvzAUeJV5r2NyoNgaSFVrDuZrWCMH08fnP/8njwuZZOC9ngFn+shbczCjiHYeEwBGBpwTt3+V9MZu840CT7uc9ehY4fl+2Zq+Sl4zL+fwf/k9/MtnG3gj4J7UxORAMTaYSdYUpMMaOZgNdH77bBdTL9TuwdwK/7aj1S1C24t15JTOrJsmOTRTkNatrp/tnLyc9fl+GUrZ01fJ6+2pcff7v3x1/Ix70llYkKbYyqYT7voGdxFcSFcrTQxn9OMfYbrN5DDsW8lcnVZqsyCdrV9zyJtppSYK0uYSXX/dwcYFcMbrLw7j+tXL+HL7AH91ZaLT4XQtJgeKrWw64a5vKJYqSCf7kEqEM1gWEUy/MIRfPn6ON//Qv8Nta4b7k+5qa8Cz0U+7i+BO2fDHTCs1MyVktlg1rUIMG/sqGSKCH1x/s9NhdD1OK1FsZdNJ7JePcHyssHd4FNoaB+Mf3r2Cb74+gb9588W2HmdkwFdzOKhABIFagHsNpBJIJ/pQqFOQvphNIdlEoryYTUOkmlAMG/sqUbg4cqDYMsXn/fIRiqVKaPUG4+3pcbw93f6cds200n4ZQ5lk21fZiIhuCe4/sZeaulIJcC4NHc2msbl7suZg87QShYMjB4otkwyKpYozcgjpSqWwDfensHNQxrFetRVGR1YjN5CqGTls7LbWC2psKO0WsQ2bp5UoHEwOFFum+Lx3GM3IISzDA0kcq+pajJ2D9juyGrlsbXJwmu61kBwGM+7aCCNfLCOVEAyF1KuK7MPkQLF1YuRQsnfk4G++t73ffkfW6mOn61yt1FzrDOO0kUMuG2z3O+oOTA4UW27NoXSE4mHF3TrUNm5/JV2U3g6hI6vhFLuryaFydIytvXJLI4fxoQw26tQcbOvISuGKLDmIyIKIzIvIzTq35fTtCyKy5Pn5lojc9/6MKCgzrVQsHdU0n7OJ25n1wDtyCHNaqfqpP7/X/OpoY2wwje2DCkqVY/dnW8Uy6w0xF0lyEJEFAFBKrQIoiMi87y7vARhVSn2s739D//y6UuqqUupWFHFRb3G3Cj2sYK9UCW0BXNhGfFuFhl2QLpaO3BN7dXV0K9NKtWsdbO2rROGJ6qPUWwA+1N+vA5gBsGpuVEote+47CeCO/j4nIpNKqfV6D6qTyA0AmJiYwNraWqDgdnd3Ax8bJcbVmkZxPdtzToj3f/lrbO+VsPn0CdbWNjsel5+J8z8+/RWSz36D3YMKtp5+gbW1r9qO5dkXTsL50U9/hkS5iIf/dg8A8P+fPcTa5n839RhPnjrTXT/+2b/i5WEnwT4t7OGl9EFo74tufY91ynnEFVVy8C8ZHat3JxGZBJD3JINRAHkRuaOUWvTfXyeVZQCYnZ1Vc3NzgYJbW1tD0GOjxLha0yiujd1D4OeruPzKNEq/eogr069gbu61jsflV9gr4ebPV/DiK9OYnb0M9eOf4I0r05j7i8m2Y9n+r9/hhw8/xet/MovHD+/jpcuvAvd+gb/+8z/FdJP7HFz4PI9/+vTf8cqVr+Mbr12CUgp7P/kR/mj6ZczNXWk7RqB732Odch5xRVVzKMA50Tey4E0CSqllpVQBzlTUQkSxUY8w00hmda+tBekL/dVpJbd1RojTSgDcy1ndaaVWrlbS9zUL4XYOK6gcK04rxVxUfy33UB09TAJY8d9BRBaUUrf19/P6fnldh4h+7E+x159MQAT4SncUzVp6KWuiT3Ahk8Tz/bJno5/wCtKAkxyScOoGiT5x6xzNMFc2mcRS0K0zbOzISuGJZOSgT/CTphCtC9MQkRX9dR7Akr4y6b4+7CN4itemWE0UVF+fIJtKuJdh2jpyAJwrlrYPyqF1ZDVy7p4OeuRQPMToYLql1hxDmSTSyT5s6IVw+b3mG/dR94rsr8WMCnw/u6a/rgKYqnPYqu8rUVuymaS7F4Gtl7ICOjnsV0LryGqMuCOHEsbReusMwOnRND5YXQi35bbO4MghzrgIjmItm064u5iF3ZU1TMP9SafmYDb6CWnkcCGThEj1MtlWW2cYY0MZt+Zg1k2wI2u8MTlQrGXTSbfmYP3I4aCMnQOzRWg4sfbp+oKZVmq1dYYxNpR2C/umXTenleKNyYFibTCdgG52anVyMG0unu+HmxyAk51ZN3dLgT7xjw6m3UVwhb0S+iS80Q3ZicmBYm3AM5VkcwfR4f6Ue7XSUCbZ1EY8zRrJOs33yscKO4cVjAeZVvIkhy3ddK/d/SbIbkwOFGveK5Rs7coKOJeuFktHyBcPW7rMtBm5gRSe75WwU3KGUK20zjBGBzPYLx9hv3TEvko9gsmBYs27tsHW/RyA6hTN4639UKeUAN18b7+M7UOdHAJNKznxbRYP2VepRzA5UKyZkcNAKoGExdMgZrTweGs/kpFDYa+MbXfkECQ5OKONrWIZW3tlJocewORAsWZaaNhcjAaq6xq+3D4IPTmMZNPOAjuTHAJcrWSK2JvFQ2wVS7xSqQcwOVCsmamkgbTdb/Vhz1RSWAvgjJGBFJQCnhbbGTk4x+SLJWdaiWscYs/uvxiiNpkidJ/l21mOeD6JRzGtBABPisdIJ/oCXbVlksMXW/s4rByzIN0DmBwo1sylrEmL6w3AyTUDYa8fMCfyJ8VjjA0F2/d5uD+JZJ/g0Ve7AMAtQnsAkwPFmilI23ylEnByKmkkpI6shkkOXxZVoCklwOmvdHEwjfWNon5MJoe4Y3KgWDNTNDZfqQSc7PsUfs3BOZEfqepVR0GMDabx6JkzcmBBOv6YHCjWXp0YAgC8+8df63AkZ/NO9YQ9n+99vPE2Csmjg2kUS0fu9xRvdo+1idp0+WIWv/jetdCLvFH62vBAqI/n/d2DTisBJzf34bRS/HHkQLGXywYrwnbKH4z0h/p4qUQfzKxakNYZxtiJ5NA9yZaCYXIgssStd6/g7amxSE68pjNtO9NB5tiBVAKpEBsDkp04rURkiffnpvD+XL0NEsMzMRx8VGJGDl00CKM2MP0T9ZAX25iyMjWHY6XCCocsxuRA1AO+NXMZAuCli8GL3WZaibmhN3BaiagH/OO33sA3RvJtLQY0DfuYHHpDZMlBRBYAFADMKKVuN3N7o2OIKJhUog/DmfaKBWbh26ULwa94ou4RybSSPslDKbUKoCAi841ub3QMEXXWpQsZ/P38q/jnv/2zTodC50BUBGNEEVkC8KFS6oE+yZ8YCdS7HcDYWcfo424AuAEAExMTVz/44INA8e3u7mJoaCjQsVFiXK1hXK2xNS7A3tjiGNc777xzXyk12+h+UU0r5Xz/Hmvi9kbHQCm1DGAZAGZnZ9Xc3Fyg4NbW1hD02CgxrtYwrtbYGhdgb2y9HFdUVysVAIy2eHujY4iI6JxENXK4h+pIYBLAShO35xocQ0RE5ySSkYNS6mMAk6aorIvMEJGV024/7RgiIjp/kV3KWu9SVKXUtQa38/JVIiILcIU0ERHVYHIgIqIaTA5ERFQjkkVw50FEvgLwecDDxwFshBhOWBhXaxhXa2yNC7A3tjjG9bJS6lKjO3VtcmiHiHzSzArB88a4WsO4WmNrXIC9sfVyXJxWIiKiGkwORERUo1eTw3KnAzgF42oN42qNrXEB9sbWs3H1ZM2BiIjO1qsjByIiOgOTAxER1WByICKiGj2XHERkQW9LerPTsXjpmKxqUy4iOf16Lejd+6yhX6952+IybItLRLZE5L6Fcc2Y91inYzF0TI/062XVa+Y5f92I+rl6KjnYvE+1pS3K3wMwqtup4zzekM0QkRkA1/RrNiMik52OyUu/r6yKCcB1pdRVpdStTgfis+hp12/LazaqlJpSSl0F8B0AdzodEOC+r9b1+35d/x1EpqeSA4C3AKzr79fh7F1Np1BKLeutWQHnZGdFAlNKPVBK3RKRHJw/lvWGB50TfYKzJh6PnEUnXwDuh437IjKplLpty/9H3we1SVviAvAJgLs6KUwqpR5E+WS9lhwa7lNNtfRJJW/RH4kxC2d7WZvYdDLxGgWQFxErPgVrU/q/vIjc0cneGiJyw4yabaCUKsAZxdyF87pFqteSA/epDmZBKbXY6SD89Ce8nC3z1SIyb+n0oBkFFuBMp1rxemmPdFz3AVgxbelxWKjy7QAAAzNJREFUrfFdzo/+/7aqlJry/DsyvZYcGu1tTT4ismB26LOlRiMiS576h00JP6+LhQtw5tCtmLYUkRueE8lmR4M56Z7n+xwsGgXaNorRvFNJ30fE7/ueSg4271Ot/3hnbfpUp1+nJXPVRqfj8bgDpyA3DyDnqYt0lK6FrML5o7Xp5PIRPBdg2DJVouPIeeKy4v+jNgog3+kgfJZ1op8H8F7UrxfbZxARUY2eGjkQEVFzmByIiKgGkwMREdVgciAiohpMDkREVIPJgchHN15bMl9bPPbGWetBvC0sgjz+WY9br/eVfo4Zffsd3bhtRf9+CyJyN4znp/hJdjoAIlvpBUdh969ZAnA9gsefh9N7x29WKbWsFzMuAoCIfBfA95VSBRGxZuEZ2YXJgbqGXnG8BOeEOq+7ZsLz6TevlFrUn85vwVnI9EMAf2eOgbOA7iqczpvXffdd8S4s0s/3bTgrea/p+8wopaY8z7kCZ5HZXTgrfHM6xnrx3wQwr/sb3YKzSv/bAD70/l7+GH2/44p/8ZOOcxHOoq3Tks2JBZ+6ZQVQP6EQcVqJuo9uO73q2Zfjjj6JrnimVubhtFt+7D0GzorqRegVzEqpdaXUoj6+bjtrpdTHnt5S1/VzfqiPuQqnJ5Abwxlx3wbwiX6+mk/sp8VY5/n8xz2A0532xMpnvdr+I32fgv7ZiRFGvTiIACYH6j6m46npEfQWqie7B6iePFc9Jz7vMeb7gumfo+fkz2z6pk+0eX0ingJwTdcLCvrf7U4PnRWj//n8seVQv9XDaJ2T/zWwpxg1gdNK1O3uwRklfKy/PtI/b+oTsU4KOQDLcKZm6t0nB+C7ZhoLTgfRvGcTpJtw9gZZRzRt4E88Xx2zcEZNM6Yx2xn7SszDadpGdCYmB+pqSqnbInJXRBYBFDx1hGatw5nvP+ukvgQAZi8EXde4IyKmDvEdAD/1/PtMun7Q9I5suqDsPp+pQ/h+h3mcTAbzvvpJTt9nEtVkSnQqNt4jiiG9UY1NXU6py7DmQBQzuuhsTTt66k4cORARUQ2OHIiIqAaTAxER1WByICKiGkwORERUg8mBiIhqMDkQEVGN3wN6ohT4SRKspAAAAABJRU5ErkJggg==
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Doppler-Power-Spectrum">Doppler Power Spectrum<a class="anchor-link" href="#Doppler-Power-Spectrum">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Still working on scaling and centering spectrum properly.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[193]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">jakes_fading</span><span class="p">(</span>
    <span class="n">NN_sym</span> <span class="o">=</span>  <span class="mi">512</span><span class="p">,</span> <span class="c1"># number of symbols</span>
    <span class="n">NN_sps</span> <span class="o">=</span> <span class="mi">1024</span><span class="p">,</span> <span class="c1"># number of samples per symbol</span>
    <span class="n">NN_pth</span> <span class="o">=</span>  <span class="mi">256</span><span class="p">,</span> <span class="c1"># number of paths</span>
    <span class="n">FF_dop</span> <span class="o">=</span>    <span class="mi">1</span><span class="p">,</span> <span class="c1"># maximum doppler shift (Hz)</span>
    <span class="n">FF_car</span> <span class="o">=</span>    <span class="mi">0</span><span class="p">,</span> <span class="c1"># carrier frequency (Hz)</span>
    <span class="n">FF_sym</span> <span class="o">=</span>    <span class="mi">4</span>  <span class="c1"># symbol rate (baud)</span>
<span class="p">)</span>

<span class="c1"># Welch Spectrum</span>
<span class="n">nperseg</span> <span class="o">=</span> <span class="n">NN_sam</span><span class="o">/</span><span class="mi">2</span> <span class="c1"># frequency range [-NN_sps/2,NN_sps/2]</span>
<span class="n">ff</span><span class="p">,</span> <span class="n">Sx</span> <span class="o">=</span> <span class="n">signal</span><span class="o">.</span><span class="n">welch</span><span class="p">(</span><span class="n">xx_n</span><span class="p">,</span>
                      <span class="n">fs</span> <span class="o">=</span> <span class="n">FF_sam</span><span class="p">,</span>
                      <span class="n">return_onesided</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
                      <span class="n">nperseg</span> <span class="o">=</span> <span class="n">nperseg</span><span class="p">)</span>

<span class="n">k</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="n">ff</span><span class="o">.</span><span class="n">size</span><span class="p">)</span> <span class="c1"># frequency index</span>
<span class="n">ff_k</span> <span class="o">=</span> <span class="n">ff</span><span class="p">[</span><span class="n">np</span><span class="o">.</span><span class="n">argsort</span><span class="p">(</span><span class="n">ff</span><span class="p">)]</span>
<span class="n">Sx_k</span> <span class="o">=</span> <span class="n">Sx</span><span class="p">[</span><span class="n">np</span><span class="o">.</span><span class="n">argsort</span><span class="p">(</span><span class="n">ff</span><span class="p">)]</span>


<span class="n">fig</span><span class="p">,</span> <span class="n">axs</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">()</span>
<span class="n">axs</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="sa">r</span><span class="s2">&quot;Power spectral density of $x(t)$&quot;</span><span class="p">)</span>
<span class="n">axs</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="sa">r</span><span class="s2">&quot;frequency $f$&quot;</span><span class="p">)</span>
<span class="n">axs</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="sa">r</span><span class="s2">&quot;power $|S_x(t)|^2$&quot;</span><span class="p">)</span>
<span class="n">axs</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">ff_k</span><span class="p">,</span><span class="n">Sx_k</span><span class="p">)</span>
<span class="n">axs</span><span class="o">.</span><span class="n">axvline</span><span class="p">(</span><span class="n">FF_car</span> <span class="o">+</span> <span class="n">FF_dop</span><span class="p">,</span><span class="n">linestyle</span> <span class="o">=</span> <span class="s2">&quot;--&quot;</span><span class="p">,</span><span class="n">linewidth</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span><span class="n">color</span><span class="o">=</span><span class="s2">&quot;blue&quot;</span><span class="p">)</span>
<span class="n">axs</span><span class="o">.</span><span class="n">axvline</span><span class="p">(</span><span class="n">FF_car</span><span class="p">,</span><span class="n">label</span><span class="o">=</span><span class="s2">&quot;$f_</span><span class="si">{c}</span><span class="s2">$&quot;</span><span class="p">,</span><span class="n">linestyle</span> <span class="o">=</span> <span class="s2">&quot;--&quot;</span><span class="p">,</span><span class="n">linewidth</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span><span class="n">color</span><span class="o">=</span><span class="s2">&quot;blue&quot;</span><span class="p">)</span>

<span class="c1"># Plot theoretical doppler spectrum</span>
<span class="k">def</span> <span class="nf">Sx_theory</span><span class="p">(</span><span class="n">f</span><span class="p">,</span><span class="n">f_dop</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
    <span class="n">func</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="mi">1</span><span class="o">/</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">pi</span><span class="o">*</span><span class="n">f_dop</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">sqrt</span><span class="p">(</span><span class="mi">1</span><span class="o">-</span><span class="p">(</span><span class="n">x</span><span class="o">/</span><span class="n">f_dop</span><span class="p">)</span><span class="o">**</span><span class="mi">2</span><span class="p">))</span>
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">piecewise</span><span class="p">(</span><span class="n">f</span><span class="p">,[</span><span class="n">np</span><span class="o">.</span><span class="n">abs</span><span class="p">(</span><span class="n">f</span><span class="p">)</span><span class="o">&lt;</span><span class="n">f_dop</span><span class="p">],[</span><span class="n">func</span><span class="p">,</span><span class="mi">0</span><span class="p">])</span>
<span class="n">eps</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">finfo</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">float32</span><span class="p">)</span><span class="o">.</span><span class="n">eps</span>
<span class="n">f</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linspace</span><span class="p">(</span><span class="o">-</span><span class="p">(</span><span class="n">FF_car</span><span class="o">+</span><span class="n">FF_dop</span><span class="p">)</span><span class="o">/</span><span class="n">FF_sym</span><span class="o">-</span><span class="n">eps</span><span class="p">,(</span><span class="n">FF_car</span><span class="o">+</span><span class="n">FF_dop</span><span class="p">)</span><span class="o">/</span><span class="n">FF_sym</span><span class="o">+</span><span class="n">eps</span><span class="p">,</span><span class="mi">256</span><span class="p">)</span>
<span class="n">axs</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">f</span><span class="p">,</span><span class="n">FF_sym</span><span class="o">*</span><span class="n">Sx_theory</span><span class="p">((</span><span class="n">f</span><span class="o">-</span><span class="n">FF_car</span><span class="p">)</span><span class="o">*</span><span class="n">FF_sym</span><span class="p">,</span><span class="n">f_dop</span><span class="o">=</span><span class="n">FF_dop</span><span class="p">),</span><span class="n">label</span><span class="o">=</span><span class="s2">&quot;theory&quot;</span><span class="p">)</span>

<span class="n">axs</span><span class="o">.</span><span class="n">set_xlim</span><span class="p">(</span><span class="o">-</span><span class="mi">2</span><span class="o">*</span><span class="p">(</span><span class="n">FF_car</span><span class="o">+</span><span class="n">FF_dop</span><span class="p">)</span><span class="o">/</span><span class="n">FF_sym</span><span class="p">,</span><span class="mi">2</span><span class="o">*</span><span class="p">(</span><span class="n">FF_car</span><span class="o">+</span><span class="n">FF_dop</span><span class="p">)</span><span class="o">/</span><span class="n">FF_sym</span><span class="p">)</span>

<span class="n">axs</span><span class="o">.</span><span class="n">legend</span><span class="p">()</span>
<span class="n">fig</span><span class="o">.</span><span class="n">tight_layout</span><span class="p">()</span>
<span class="n">fig</span><span class="o">.</span><span class="n">savefig</span><span class="p">(</span><span class="s2">&quot;./plots/doppler_spectrum.png&quot;</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Welch periodogram properties:&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;frequency spacing:     </span><span class="si">{}</span><span class="s2"> Hz&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">ff_k</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">-</span> <span class="n">ff_k</span><span class="p">[</span><span class="mi">0</span><span class="p">]))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Number of frequencies: </span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">ff_k</span><span class="o">.</span><span class="n">size</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;nperseg:               </span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">nperseg</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Welch periodogram properties:
frequency spacing:     0.015625 Hz
Number of frequencies: 262144
nperseg:               262144.0
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
    </div>
  </div>
</body>

 


</html>
