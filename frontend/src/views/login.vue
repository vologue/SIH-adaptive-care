<template>
  <div class="backgroundc">
  <v-container style="position: relative;top:10%">
    <v-layout row align-center justify-center>
      <v-flex xs12 sm10 md6>
        <br><br><br>
        <v-card class="elevation-4" height="400px" style="border:10px;border-radius:15px">
          <v-card-title primary-title>

              <b> <h2 class="headline mb-0">Login</h2><br></b>


          </v-card-title>

          <v-card-text>

            <v-form ref="loginForm" lazy-validation>
              <v-text-field prepend-icon="email" label="E-mail" v-model="email" required></v-text-field>
              <v-text-field prepend-icon="lock" label="Password" :rules="passwordRules" v-model="password" type="password" required> </v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn :loading="loading" :disabled="loading" color="primary" @click="login">Login</v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    data() {
      return {

      }
    },

    computed: {


    },
    methods: {

    }
  }

</script>

<style scoped>
  .backgroundc {
    background-image: url("wall1.png");
    background-size:40%;

  }

</style>
