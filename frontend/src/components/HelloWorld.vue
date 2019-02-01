<template>
  <v-container style="position: relative;top:10%">
    <v-layout row align-center justify-center>
      <v-flex xs12 sm10 md6>
        <v-card class="elevation-3" height="400px" style="border:10px;border-radius:15px">
          <v-card-title primary-title>
            <div>
              <b> <h2 class="headline mb-0">Login</h2><br></b>
              <div>Use your SRM ID</div>
            </div>
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
</template>
