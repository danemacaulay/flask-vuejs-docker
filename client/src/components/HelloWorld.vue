<template>
  <div id="app" class="container">
    {{msg}}
  </div>
</template>

<script>
import Axios from 'axios'

export default {
  components: {
  },
  data: function () {
    return {
      msg: ''
    }
  },
  methods: {
    getMsg() {
      Axios.get('/services/health-check').then((resp) => {
        this.msg = resp.data.msg
      })
    },
  },
  mounted() {
    this.getMsg()
  }
}
</script>

<style>

</style>
