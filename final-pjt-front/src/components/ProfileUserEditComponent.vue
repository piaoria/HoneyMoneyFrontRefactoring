<template>
  <v-card prepend-icon="mdi-account" title="User Profile" :style="{ maxHeight: '1000px', overflowY: 'auto' }">
    <v-card-text>
      <v-form @submit.prevent="submitForm">
        <v-row>
          <v-col cols="12" md="4" sm="6">
            <v-text-field label="Nickname*" v-model="form.nickname" required></v-text-field>
          </v-col>
          <v-col cols="12" md="4" sm="6">
            <v-text-field label="Age*" type="number" v-model="form.age" required></v-text-field>
          </v-col>
          <v-col cols="12" md="4" sm="6">
            <v-text-field label="Salary*" type="number" v-model="form.salary" required></v-text-field>
          </v-col>
          <v-col cols="12" md="4" sm="6">
            <v-text-field label="Wealth*" type="number" v-model="form.wealth" required></v-text-field>
          </v-col>
          <v-col cols="12" md="4" sm="6">
            <v-text-field label="Password*" type="password" v-model="form.password1" required></v-text-field>
          </v-col>
          <v-col cols="12" md="4" sm="6">
            <v-text-field label="Confirm Password*" type="password" v-model="form.password2" required></v-text-field>
          </v-col>
          <v-col cols="12" sm="6">
            <v-select :items="[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]" label="Tendency*" v-model="form.tendency" required></v-select>
          </v-col>
          <v-col cols="12" sm="6">
            <v-select :items="[6, 12, 24, 36]" label="Desire Period*" v-model="form.desirePeriod" required></v-select>
          </v-col>
          <v-col cols="12">
            <v-file-input prepend-icon="mdi-camera" label="Profile Image" accept="image/" v-model="form.profile_img"></v-file-input>
          </v-col>
        </v-row>
        <small class="text-caption text-medium-emphasis">*indicates required field</small>
      </v-form>
    </v-card-text>
    <v-divider></v-divider>
    <v-card-actions>
      <v-row justify="space-between" align="center" class="w-100">
        <v-col cols="auto">
          <v-btn color="red" text="Accounts Delete" variant="plain" @click="deleteAccount"></v-btn>
        </v-col>
        <v-col cols="auto">
          <v-btn color="primary" text="Save" variant="tonal" @click="submitForm"></v-btn>
        </v-col>
      </v-row>
    </v-card-actions>
  </v-card>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import { useUserStore } from "@/stores/user";
import { storeToRefs } from "pinia";
import { useRouter } from "vue-router";
const emit = defineEmits(["close-dialog"]);
const userStore = useUserStore()
const { userProfile } = storeToRefs(userStore);
const router = useRouter();

const form = ref({
  nickname: `${userProfile.value.nickname}`,
  age: `${userProfile.value.age}`,
  salary: `${userProfile.value.salary}`,
  wealth: `${userProfile.value.wealth}`,
  password1: `${userProfile.value.password1}`,
  password2: `${userProfile.value.password2}`,
  tendency: `${userProfile.value.tendency}`,
  desirePeriod: `${userProfile.value.desirePeriod}`,
  profile_img: null, // 프로필 이미지
});

const submitForm = async () => {
  const formData = new FormData();
  formData.append("nickname", form.value.nickname);
  formData.append("age", form.value.age);
  formData.append("salary", form.value.salary);
  formData.append("wealth", form.value.wealth);
  formData.append("password1", form.value.password1);
  formData.append("password2", form.value.password2);
  formData.append("tendency", form.value.tendency);
  formData.append("desirePeriod", form.value.desirePeriod);
  if (form.value.profile_img) {
    formData.append("profile_img", form.value.profile_img);
  }
  axios({
    method: "put",
    url: `http://127.0.0.1:8000/accounts/${userProfile.value.username}/`,
    data: formData,
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
  })
    .then((res) => {
      swal("성공적으로 저장되었습니다!", "You clicked the button!", "success");
      emit("close-dialog");
      userStore.getProfile(); // 업데이트된 프로필을 다시 가져옵니다.
    })
    .catch((err) => {
      console.log(err);
    });
};
const deleteAccount = function () {
  swal({
    title: "정말 떠나실 건가요..?",
    text: "꿀은 숙성될 수록 비싸답니다",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  }).then((willDelete) => {
    if (willDelete) {
      swal("꿀통이 완전히 제거되었습니다", {
        icon: "success",
      });
      axios({
        method: "delete",
        url: `http://127.0.0.1:8000/accounts/user/delete/${userProfile.value.username}/`,
        headers: {
          Authorization: `Token ${userStore.token}`,
        },
      })
        .then((res) => {
          userStore.logoutUser();
          router.push({ name: "MainView" });
        })
        .catch((err) => {
          console.log(err);
        });
    } else {
      swal("꿀통을 지키셨어요!");
    }
  });
};
</script>

<style scoped></style>
