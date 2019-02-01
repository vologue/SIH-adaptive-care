<template>
<div class="backgroundc">
  <v-container fill-height>
    <v-layout row align-center justify-center>
      <v-flex xs12 sm10 md6>

      <v-stepper v-model="e1" style="border:10px;border-radius:15px">

                    <v-stepper-header>
                      <v-stepper-step :complete="e1 > 1" step="1">Personel</v-stepper-step>
                      <v-divider></v-divider>

                      <v-stepper-step :complete="e1 > 2" step="2">Image</v-stepper-step>

                      <v-divider></v-divider>


                </v-stepper-header>


                 <v-stepper-items>



                 <v-stepper-content step="1">

                           <v-card-text>

                             <v-form ref="form1" v-model="valid1" lazy-validation>
                               <v-text-field prepend-icon="person" v-model="name" :counter="20" label="Name"  :rules="nameRules" type="text"  required ></v-text-field>
                               <v-text-field  prepend-icon="email" label="E-mail"  v-model="email" :rules="emailRules"  required ></v-text-field>
                               <v-textarea required :rules="addRules" auto-grow v-model="address" prepend-inner-icon="notes" label="Permanent Address" required></v-textarea>
                               <v-select prepend-icon="notes" v-bind:items="prob" v-model="prob" label="Problem"></v-select>
                            <v-text-field  prepend-icon="phone" v-model="Mob_no" :counter="10" label="Mobile Number"  :rules="mobRules" type="text"  required ></v-text-field>

                               </v-form>

                             </v-card-text>
                          <v-btn color="primary" :disabled="!valid1"  @click="continu">Next</v-btn>
                      <v-btn flat   @click="reset1">RESET</v-btn>


                      </v-stepper-content>
                      <v-stepper-content step="2">
                        <v-card-text>


                       <br><br><br><br><br>
                       <br><br><br><br><br>

                       <br><br><br><br><br>
                       <br><br><br><br><br>

                        </v-card-text>

                      </v-stepper-content>
                    </v-stepper-items>

                  </v-stepper>


     </v-flex>
    </v-layout>'

  </v-container>
</div>

</template>

<script>
  import axios from 'axios'
  export default {
    data() {
      return {
        name: '',
        email: '',
        Mob_no: '',
        address: '',
        prob:['Skin'],
        e1:0,
        valid1:true,
 gradient: 'to top right, rgba(63,81,181, .7), rgba(25,32,72, .7)',

        nameRules: [
          v => !!v || 'Name is required',
          v => v.length <= 20 || 'Name must be less than 20 characters'
        ],
        emailRules: [
        v => !!v || 'E-mail is required',
        v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid'
      ],
      mobRules: [
          v => !!v || 'Mobile Number is required',
          v => v.length >= 10 || 'Please enter the correct Mobile Number'
        ],
        addRules: [
          v => !!v || 'Address is required',
        ],

      }
    },

    computed: {


    },
    methods: {
      continu() {

        if (this.$refs.form1.validate()) {
          this.e1 = 2
        }
      },
      reset1() {
        this.$refs.form1.reset()
      },

    }
  }

</script>

<style scoped>
  .backgroundc {
    background-image: url("wall1.png");
    background-size:40%;

  }

</style>
