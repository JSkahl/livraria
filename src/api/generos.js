import axios from 'axios';
export default class GenerosApi {
  async buscarGeneros() {
    const { data } = await axios.get('/generos/');
    return data;
  }
  async adicionarGenero(genero) {
    const { data } = await axios.post('/generos/', genero);
    return data;
  }
  async atualizarGenero(genero) {
    const { data } = await axios.put(`/generos/${genero.id}/`, genero);
    return data;
  }
  async excluirGenero(id) {
    const { data } = await axios.delete(`/generos/${id}/`);
    return data;
  }
}
