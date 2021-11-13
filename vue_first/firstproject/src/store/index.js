import Vuex from 'vuex'
import Vue from 'vue'
import axios from 'axios'

Vue.use(Vuex);

const actions = {
    getFilmInfo(context) {
        axios.get('film.json').then(res => {
            let filmInfo = res.data
            context.commit('GET_FILM_INFO', filmInfo)
        }, err => {
            console.log(err.message)
        })
    }
}

const mutations= {
    ['GET_FILM_INFO'](state, val) {
        state.filmInfo = val
    }
}

const state = {
    filmInfo: []
}

const getters = {

}

export default new Vuex.Store({
    actions,
    mutations,
    state,
    getters
})