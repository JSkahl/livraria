<template>
  <header>

    <router-link :to="{ name: 'home' }">Home</router-link>
      <div class="espaco-header"></div>
    <router-link to="/generos">Generos</router-link>
      <div class="espaco-header"></div>
    <router-link to="/editoras">Editoras</router-link>
      <div class="espaco-header"></div>
    <router-link to="/autores">Autores</router-link>
      <div class="espaco-header"></div>
    <router-link to="/livros">Livros</router-link>


  </header>
  <main>
    <RouterView/>
  </main>
</template>

<style>
.espaco-header {
  width: 10px;
  height: 10px;
  display: inline-block
}
</style>