<template>
  <v-container align="center">
    <v-avatar :image="profileImg" size="200" alt="User Profile Image" cover></v-avatar>
    <v-card-title class="mt-3 ibm-plex-sans-kr-bold">
      <h2>{{ userProfile.nickname }} 님</h2>
    </v-card-title>
    <v-card-text class="ibm-plex-sans-kr-bold">
      <h3>{{ userProfile.username }} (만 {{ userProfile.age }}세)</h3>
    </v-card-text>
  </v-container>
</template>

<script setup>
defineProps({
  userProfile: Object,
  profileImg: String,
});
</script>

<style scoped></style>

