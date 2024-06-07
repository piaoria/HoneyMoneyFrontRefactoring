<template>
  <v-card class="mx-auto" width="1000">
    <template v-slot:subtitle>
      <v-row>
        <v-col cols="4"></v-col>
        <v-col align="center" cols="4">
          <div class="my-2 custom-subtitle ibm-plex-sans-kr-regular">{{ savingStore.getSavingDetail?.kor_co_nm }} ({{ savingStore.getSavingDetail?.dcls_month }})</div>
        </v-col>
      </v-row>
    </template>
    <template v-slot:title>
      <v-row align="center" justify="space-between">
        <v-col align="center"></v-col>
        <v-col align="center" class="pb-0 my-2">
          <span class="font-weight-black ibm-plex-sans-kr-regular">
            <h2>{{ savingStore.getSavingDetail?.fin_prdt_nm }}</h2>
          </span>
        </v-col>
        <v-col align="center" class="pb-0 mt-2"></v-col>
      </v-row>
    </template>
    <hr />
    <v-row justify="center" align="center">
      <v-col cols="3" class="d-flex justify-center">
        <v-tooltip activator="parent" location="top">
          <template v-slot:activator="{ on, attrs }">
            <v-img class="mb-0" :src="jar" width="40px" height="40px" :style="{ display: 'inline-block', marginLeft: '8px' }" v-bind="attrs" v-on="on"></v-img>
          </template>
          꿀통에 담은 이용자 수
        </v-tooltip>
      </v-col>
      <v-col>
        <v-card-text v-if="savingStore.getSavingDetail.interest_user" class="">{{ savingStore.getSavingDetail?.interest_user.length }} 명</v-card-text>
      </v-col>
    </v-row>
    <hr />
    <v-row justify="center" align="center">
      <v-col cols="3" class="d-flex justify-center">
        <v-card-text class="text-style" align="center">가입 방법</v-card-text>
      </v-col>
      <v-col>
        <v-card-text class="">{{ savingStore.getSavingDetail?.join_way }}</v-card-text>
      </v-col>
    </v-row>
    <hr />
    <v-row justify="center" align="center">
      <v-col cols="3" class="d-flex justify-center">
        <v-card-text class="text-style" align="center">만기 후 이자율</v-card-text>
      </v-col>
      <v-col>
        <v-card-text class="me-12">{{ savingStore.getSavingDetail?.mtrt_int }}</v-card-text>
      </v-col>
    </v-row>
    <hr />
    <v-row justify="center" align="center">
      <v-col cols="3" class="d-flex justify-center">
        <v-card-text class="text-style" align="center">우대 조건</v-card-text>
      </v-col>
      <v-col>
        <v-card-text class="me-12">{{ savingStore.getSavingDetail?.spcl_cnd }}</v-card-text>
      </v-col>
    </v-row>
    <hr />
    <v-row justify="center" align="center">
      <v-col cols="3" class="d-flex justify-center">
        <v-card-text class="text-style" align="center">가입 대상</v-card-text>
      </v-col>
      <v-col>
        <v-card-text class="">{{ savingStore.getSavingDetail?.join_member }}</v-card-text>
      </v-col>
    </v-row>
    <hr />
    <v-row justify="center" align="center">
      <v-col cols="3" class="d-flex justify-center">
        <v-card-text class="text-style" align="center">가입 제한</v-card-text>
      </v-col>
      <v-col>
        <v-card-text class="">
          {{ savingStore.getSavingDetail?.join_deny == 1 ? "제한없음" : savingStore.getSavingDetail?.join_deny == 2 ? "서민전용" : savingStore.getSavingDetail?.join_deny == 3 ? "일부제한" : "기타" }}
        </v-card-text>
      </v-col>
    </v-row>
    <hr />
    <v-row justify="center" align="center">
      <v-col cols="3" class="d-flex justify-center">
        <v-card-text class="text-style" align="center">최고 한도</v-card-text>
      </v-col>
      <v-col>
        <v-card-text class="">
          {{
            savingStore.getSavingDetail?.max_limit === null
              ? "한도 없음"
              : `${new Intl.NumberFormat("ko-KR", {
                  style: "currency",
                  currency: "KRW",
                }).format(savingStore.getSavingDetail?.max_limit)}`
          }}
        </v-card-text>
      </v-col>
    </v-row>
    <hr />
    <v-row justify="center" align="center">
      <v-col cols="3" class="d-flex justify-center">
        <v-card-text class="text-style" align="center">기타 유의사항</v-card-text>
      </v-col>
      <v-col>
        <v-card-text class="me-12">{{ savingStore.getSavingDetail?.etc_note }}</v-card-text>
      </v-col>
    </v-row>
    <hr />
    <v-row justify="center" align="center">
      <v-col>
        <ChartComponent v-if="savingStore.getSavingDetailOption" :data="savingStore.getSavingDetailOption" :title="savingStore.getSavingDetail.fin_prdt_nm" />
      </v-col>
    </v-row>
    <hr />
    <v-card-actions class="justify-center">
      <v-btn class="mb-6" @click="closeDialog">OK</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup>
import { useSavingStore } from "@/stores/saving";
import jar from "@/assets/jar.png";
import ChartComponent from "@/components/SavingChartComponent.vue";

const emit = defineEmits(["close-dialog"]);
const savingStore = useSavingStore();

const closeDialog = function () {
  // 상위 컴포넌트 dialog 변수 변경
  emit("close-dialog");
};
</script>

<style scoped>
hr {
  margin-top: 10px;
  margin-bottom: 10px;
  margin-left: 40px;
  margin-right: 40px;
  box-shadow: 1px 1px 1px rgba(193, 193, 193, 0.435);
  border: 1px solid rgba(255, 255, 255, 0);
}
.text-style {
  font-weight: bolder;
  font-size: medium;
}
</style>
