import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import GeneroView from '../views/GeneroView.vue';
import EditoraView from '../views/EditoraView.vue';
import AutorView from '../views/AutorView.vue';
import LivroView from '../views/LivroView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/generos',
      name: 'generos',
      component: GeneroView,
    },
    {
      path: '/editoras',
      name: 'editoras',
      component: EditoraView,
    },
    {
      path: '/autores',
      name: 'autores',
      component: AutorView,
    },
    {
      path: '/livros',
      name: 'livros',
      component: LivroView,
    }
  ],
});

export default router;
