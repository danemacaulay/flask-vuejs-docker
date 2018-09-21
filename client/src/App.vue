<template>
  <div id="app" class="container">
      <router-link class="logo" :to="{name: 'helloWorld'}">
          <img src="./assets/logo.png">
          <small>HELLO</small>
      </router-link>
      <div class="pull-right">
        <router-link class="nav-link" :to="{name: 'helloWorld'}">
          HelloWorld
        </router-link>
      </div>
      <router-view/>
  </div>
</template>

<style>
body {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.h1, .h2, .h3, .h4, .h5, .h6, h1, h2, h3, h4, h5, h6, label, th {
  color: #005172
}
a {
  cursor: pointer;
}
@keyframes spin {
  from { transform: scale(1) rotate(0deg); }
  to { transform: scale(1) rotate(360deg); }
}
@-webkit-keyframes spin2 {
  from { -webkit-transform: rotate(0deg); }
  to { -webkit-transform: rotate(360deg); }
}
.glyphicon.spinning {
  animation: spin 1s infinite linear;
  -webkit-animation: spin2 1s infinite linear;
}
.loader {
  height: 135px; text-align:center
}
.spinner {
  margin-top: 50px; font-size: 40px
}
.article-list .spinner {
  margin-top: 160px
}
.logo{
  display: inline-block;
}
.logo-svg {
  padding: 18px 0 18px 0;
  width: 260px;
}
.logo small {
  display: block;
  top: -12px;
  position: relative;
  color: #728d96;
}
.logo:hover {
  text-decoration: none
}
.nav-link {
  padding-left: 20px;
}
</style>
