<template>
  <v-container>
    <v-card-title class="ibm-plex-sans-kr-bold"><h4>나의 금융 정보</h4></v-card-title>
    <div class="px-4 mb-2">
      <v-chip class="chip-style mx-1 my-1">
        나의 연봉 :
        {{
          new Intl.NumberFormat("ko-KR", {
            style: "currency",
            currency: "KRW",
          }).format(userProfile.salary)
        }}
      </v-chip>
      <v-chip class="chip-style mx-1 my-1">
        나의 자산 :
        {{
          new Intl.NumberFormat("ko-KR", {
            style: "currency",
            currency: "KRW",
          }).format(userProfile.wealth)
        }}
      </v-chip>
      <v-chip class="chip-style mx-1 my-1">나의 저축 성향 : {{ userProfile.tendency }}</v-chip>
      <v-chip class="chip-style mx-1 my-1">나의 저축 희망 기간 : {{ userProfile.desirePeriod }}개월</v-chip>
    </div>
  </v-container>
</template>

<script setup>
defineProps({
  userProfile: Object,
});
</script>

<style scoped>
.chip-style {
  cursor: pointer;
}
.chip-style:hover {
  background-color: rgba(255, 162, 0, 0.199);
}
</style>
