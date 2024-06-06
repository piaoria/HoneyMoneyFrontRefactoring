<template>
  <div>
    <v-tabs class="mb-8 mt-10 custom-bg" variant="outlined" divided>
      <v-tab class="ibm-plex-sans-kr-regular" style="width: 50%" @click="Financial"><h3>나와 비슷한 금융 정보를 가진 사용자들이 가입한 상품</h3></v-tab>
      <v-tab class="ibm-plex-sans-kr-regular" style="width: 50%" @click="Age">
        <h3>{{ age }}대가 가장 많이 가입한 상품</h3>
      </v-tab>
    </v-tabs>
    <v-data-table-virtual v-if="state === 'financial'" height="600" :items="recommendFirst" class="elevation-2" item-class="hoverable-row" fixed-header>
      <template v-slot:item.상품명="{ item }">
        <v-btn class="mx-auto custom-btn" @click="showDetails(item)">{{ item.상품명 }}</v-btn>
      </template>
      <template v-if="userPeriod && userPeriod === 6" v-slot:item.6개월="{ value }">
        <v-chip :color="getColor(value)">{{ value }}</v-chip>
      </template>
      <template v-else-if="userPeriod && userPeriod === 12" v-slot:item.12개월="{ value }">
        <v-chip :color="getColor(value)">{{ value }}</v-chip>
      </template>
      <template v-else-if="userPeriod && userPeriod === 24" v-slot:item.24개월="{ value }">
        <v-chip :color="getColor(value)">{{ value }}</v-chip>
      </template>
      <template v-else-if="userPeriod && userPeriod === 36" v-slot:item.36개월="{ value }">
        <v-chip :color="getColor(value)">{{ value }}</v-chip>
      </template>
      <template v-else v-slot:item.6개월="{ value }">
        <v-chip :color="getColor(value)">{{ value }}</v-chip>
      </template>
    </v-data-table-virtual>
    <v-data-table-virtual v-if="state === 'age'" height="600" :items="recommendSecond" class="elevation-2" item-class="hoverable-row" fixed-header>
      <template v-slot:item.상품명="{ item }">
        <v-btn class="mx-auto custom-btn" @click="showDetails(item)">{{ item.상품명 }}</v-btn>
      </template>
      <template v-if="userPeriod && userPeriod === 6" v-slot:item.6개월="{ value }">
        <v-chip :color="getColor(value)">{{ value }}</v-chip>
      </template>
      <template v-else-if="userPeriod && userPeriod === 12" v-slot:item.12개월="{ value }">
        <v-chip :color="getColor(value)">{{ value }}</v-chip>
      </template>
      <template v-else-if="userPeriod && userPeriod === 24" v-slot:item.24개월="{ value }">
        <v-chip :color="getColor(value)">{{ value }}</v-chip>
      </template>
      <template v-else-if="userPeriod && userPeriod === 36" v-slot:item.36개월="{ value }">
        <v-chip :color="getColor(value)">{{ value }}</v-chip>
      </template>
      <template v-else v-slot:item.6개월="{ value }">
        <v-chip :color="getColor(value)">{{ value }}</v-chip>
      </template>
    </v-data-table-virtual>
    <!-- 예금 디테일 페이지 -->
    <v-dialog v-model="depositDialog" width="1000">
      <DepositDetailComponent @close-dialog="depositDialog = false" />
    </v-dialog>
    <!-- 적금 디테일 페이지 -->
    <v-dialog v-model="savingDialog" width="1000">
      <SavingDetailComponent @close-dialog="savingDialog = false" />
    </v-dialog>
  </div>
</template>

<script setup>
import { useRecommendStore } from "@/stores/recommend";
import { useUserStore } from "@/stores/user";
import { onMounted, ref } from "vue";
import { useDepositStore } from "@/stores/deposit";
import { useSavingStore } from "@/stores/saving";
import DepositDetailComponent from "@/components/DepositDetailComponent.vue";
import SavingDetailComponent from "@/components/SavingDetailComponent.vue";

const depositStore = useDepositStore();
const savingStore = useSavingStore();

// getColor 함수 정의
const getColor = (value) => {
  if (value >= 3) {
    return "green";
  } else if (value >= 2) {
    return "orange";
  } else {
    return "white";
  }
};
const store = useRecommendStore();
const state = ref("financial");
const userStore = useUserStore();
const userPeriod = userStore.userProfile.desirePeriod;
const depositDialog = ref(false);
const savingDialog = ref(false);
const age = ref(Math.floor(userStore.userProfile.age / 10) * 10);
const Financial = () => {
  state.value = "financial";
};
const Age = () => {
  state.value = "age";
};

onMounted(() => {
  store.getRecommendFirst();
  store.getRecommendSecond();
});

const recommendFirst = ref([]);
const recommend1 = function () {
  recommendFirst.value = store.recommendFirst.map((element) => {
    console.log("element", element);
    if (element.fin_prdt_nm.includes("예금")) {
      const type = "예금";
      const option6 = element.depositoption_set.find((option) => option.save_trm === 6);
      const intrRate6 = option6 ? option6.intr_rate : null;
      const option12 = element.depositoption_set.find((option) => option.save_trm === 12);
      const intrRate12 = option12 ? option12.intr_rate : null;
      const option24 = element.depositoption_set.find((option) => option.save_trm === 24);
      const intrRate24 = option24 ? option24.intr_rate : null;
      const option36 = element.depositoption_set.find((option) => option.save_trm === 36);
      const intrRate36 = option36 ? option36.intr_rate : null;
      return {
        유형: type,
        상품코드: element.fin_prdt_cd,
        은행: element.kor_co_nm,
        상품명: element.fin_prdt_nm,
        "6개월": intrRate6,
        "12개월": intrRate12,
        "24개월": intrRate24,
        "36개월": intrRate36,
      };
    } else if (element.fin_prdt_nm.includes("적금")) {
      const type = "적금";
      const option6 = element.savingoption_set.find((option) => option.save_trm === 6);
      const intrRate6 = option6 ? option6.intr_rate : null;
      const option12 = element.savingoption_set.find((option) => option.save_trm === 12);
      const intrRate12 = option12 ? option12.intr_rate : null;
      const option24 = element.savingoption_set.find((option) => option.save_trm === 24);
      const intrRate24 = option24 ? option24.intr_rate : null;
      const option36 = element.savingoption_set.find((option) => option.save_trm === 36);
      const intrRate36 = option36 ? option36.intr_rate : null;
      return {
        유형: type,
        상품코드: element.fin_prdt_cd,
        은행: element.kor_co_nm,
        상품명: element.fin_prdt_nm,
        "6개월": intrRate6,
        "12개월": intrRate12,
        "24개월": intrRate24,
        "36개월": intrRate36,
      };
    }
  });
};
const recommendSecond = ref([]);
const recommend2 = function () {
  recommendSecond.value = store.recommendSecond.map((element) => {
    console.log("element", element);
    if (element.fin_prdt_nm.includes("예금")) {
      const type = "예금";
      const option6 = element.depositoption_set.find((option) => option.save_trm === 6);
      const intrRate6 = option6 ? option6.intr_rate : null;
      const option12 = element.depositoption_set.find((option) => option.save_trm === 12);
      const intrRate12 = option12 ? option12.intr_rate : null;
      const option24 = element.depositoption_set.find((option) => option.save_trm === 24);
      const intrRate24 = option24 ? option24.intr_rate : null;
      const option36 = element.depositoption_set.find((option) => option.save_trm === 36);
      const intrRate36 = option36 ? option36.intr_rate : null;
      return {
        유형: type,
        상품코드: element.fin_prdt_cd,
        은행: element.kor_co_nm,
        상품명: element.fin_prdt_nm,
        "6개월": intrRate6,
        "12개월": intrRate12,
        "24개월": intrRate24,
        "36개월": intrRate36,
      };
    } else if (element.fin_prdt_nm.includes("적금")) {
      const type = "적금";
      const option6 = element.savingoption_set.find((option) => option.save_trm === 6);
      const intrRate6 = option6 ? option6.intr_rate : null;
      const option12 = element.savingoption_set.find((option) => option.save_trm === 12);
      const intrRate12 = option12 ? option12.intr_rate : null;
      const option24 = element.savingoption_set.find((option) => option.save_trm === 24);
      const intrRate24 = option24 ? option24.intr_rate : null;
      const option36 = element.savingoption_set.find((option) => option.save_trm === 36);
      const intrRate36 = option36 ? option36.intr_rate : null;
      return {
        유형: type,
        상품코드: element.fin_prdt_cd,
        은행: element.kor_co_nm,
        상품명: element.fin_prdt_nm,
        "6개월": intrRate6,
        "12개월": intrRate12,
        "24개월": intrRate24,
        "36개월": intrRate36,
      };
    }
  });
};

onMounted(() => {
  recommend1();
  recommend2();
});

const showDetails = (productInfo) => {
  console.log(productInfo);
  if (productInfo.유형 === "예금") {
    depositStore.getDepositData(productInfo.상품코드);
    depositStore.getDepositOptionData(productInfo.상품코드);
    depositDialog.value = true;
  } else if (productInfo.유형 === "적금") {
    savingStore.getSavingData(productInfo.상품코드);
    savingStore.getSavingOptionData(productInfo.상품코드);
    savingDialog.value = true;
  }
};
</script>

<style scoped>
.hoverable-row {
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.hoverable-row:hover {
  background-color: #f5f5f5;
}
</style>
