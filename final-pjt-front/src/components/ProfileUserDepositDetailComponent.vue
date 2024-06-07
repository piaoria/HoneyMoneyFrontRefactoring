<template>
  <v-card class="mx-auto" width="1000">
    <template v-slot:subtitle>
      <v-row>
        <v-col cols="4"></v-col>
        <v-col align="center" cols="4">
          <div class="my-2 custom-subtitle ibm-plex-sans-kr-regular">{{ depositStore.getDepositDetail?.kor_co_nm }} ({{ depositStore.getDepositDetail?.dcls_month }})</div>
        </v-col>
      </v-row>
    </template>
    <template v-slot:title>
      <v-row align="center" justify="space-between">
        <v-col align="center"></v-col>
        <v-col align="center" class="pb-0 my-2">
          <span class="font-weight-black ibm-plex-sans-kr-regular">
            <h2>{{ depositStore.getDepositDetail?.fin_prdt_nm }}</h2>
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
            <v-img class="mb-0 inline-block ml-2" :src="jar" width="40px" height="40px" v-bind="attrs" v-on="on" aria-label="Number of users with honey in the jar"></v-img>
          </template>
          꿀통에 담은 이용자 수
        </v-tooltip>
      </v-col>
      <v-col>
        <v-card-text v-if="depositStore.getDepositDetail.interest_user">{{ depositStore.getDepositDetail?.interest_user.length }} 명</v-card-text>
      </v-col>
    </v-row>
    <hr />
    <v-row justify="center" align="center">
      <v-col cols="3" class="d-flex justify-center">
        <v-card-text class="text-style" align="center">가입 방법</v-card-text>
      </v-col>
      <v-col>
        <v-card-text class="">{{ depositStore.getDepositDetail?.join_way }}</v-card-text>
      </v-col>
    </v-row>
    <hr />
    <v-row justify="center" align="center">
      <v-col cols="3" class="d-flex justify-center">
        <v-card-text class="text-style" align="center">만기 후 이자율</v-card-text>
      </v-col>
      <v-col>
        <v-card-text class="me-12">{{ depositStore.getDepositDetail?.mtrt_int }}</v-card-text>
      </v-col>
    </v-row>
    <hr />
    <v-row justify="center" align="center">
      <v-col cols="3" class="d-flex justify-center">
        <v-card-text class="text-style" align="center">우대 조건</v-card-text>
      </v-col>
      <v-col>
        <v-card-text class="me-12">{{ depositStore.getDepositDetail?.spcl_cnd }}</v-card-text>
      </v-col>
    </v-row>
    <hr />
    <v-row justify="center" align="center">
      <v-col cols="3" class="d-flex justify-center">
        <v-card-text class="text-style" align="center">가입 대상</v-card-text>
      </v-col>
      <v-col>
        <v-card-text class="">{{ depositStore.getDepositDetail?.join_member }}</v-card-text>
      </v-col>
    </v-row>
    <hr />
    <v-row justify="center" align="center">
      <v-col cols="3" class="d-flex justify-center">
        <v-card-text class="text-style" align="center">가입 제한</v-card-text>
      </v-col>
      <v-col>
        <v-card-text class="">
          {{ depositStore.getDepositDetail?.join_deny == 1 ? "제한없음" : depositStore.getDepositDetail?.join_deny == 2 ? "서민전용" : depositStore.getDepositDetail?.join_deny == 3 ? "일부제한" : "기타" }}
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
            depositStore.getDepositDetail?.max_limit === null
              ? "한도 없음"
              : `${new Intl.NumberFormat("ko-KR", {
                  style: "currency",
                  currency: "KRW",
                }).format(depositStore.getDepositDetail?.max_limit)}`
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
        <v-card-text class="me-12">{{ depositStore.getDepositDetail?.etc_note }}</v-card-text>
      </v-col>
    </v-row>
    <hr />
    <v-row justify="center" class="mt-2" align="center">
      <v-col>
        <ChartComponent v-if="depositStore.getDepositDetailOption" :data="depositStore.getDepositDetailOption" :title="depositStore.getDepositDetail.fin_prdt_nm" />
      </v-col>
    </v-row>
    <hr />
    <v-card-actions class="justify-center">
      <v-btn class="mb-6" @click="closeDialog">OK</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup>
import { useDepositStore } from "@/stores/deposit";
import jar from "@/assets/jar.png";
import ChartComponent from "@/components/DepositChartComponent.vue";

const emit = defineEmits(["close-dialog"]);
const depositStore = useDepositStore();

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
