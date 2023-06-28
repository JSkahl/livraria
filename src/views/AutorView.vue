<script>
import AutoresApi from "@/api/autores";
const autoresApi = new AutoresApi();
export default {
    data() {
        return {
            autores: [],
            autor: {},
        };
    },
    async created() {
        this.autores = await autoresApi.buscarAutores();
    },
    methods: {
        async salvar() {
            if (this.autor.id) {
                await autoresApi.atualizarAutor(this.autor);
            } else {
                await autoresApi.adicionarAutor(this.autor);
            }
            this.autor = {};
            this.autores = await autoresApi.buscarAutores();
        },
        editar(autor) {
            Object.assign(this.autor, autor);
        },
        async excluir(autor) {
            await autoresApi.excluirAutor(autor.id);
            this.autores = await autoresApi.buscarAutores();
        },
    },
};
</script>

<template>
    <h1>Autores</h1>
    <hr>
    <input type="text" v-model="autor.nome" placeholder="Descrição">
    <div></div>
    <input type="text" v-model="autor.email" placeholder="Email">
    <div></div>
    <button @click="salvar">Salvar</button>
    <hr>
    <ul>
    <li v-for="autor in autores" :key="autor.id">
        <span @click="editar(autor)">
            ({{ autor.id }}) - {{ autor.nome }} -
        </span>
        <button @click="excluir(autor)">X</button>
    </li>
    </ul>
</template>

<style>
</style>