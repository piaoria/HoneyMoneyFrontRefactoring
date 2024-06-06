<template>
  <v-container>
    <v-container>
      <v-row class="align-center">
        <v-col>
          <v-tabs class="mb-3" v-model="type" variant="outlined" divided>
            <v-tab class="ibm-plex-sans-kr-regular" @click="loaddata_free()"><h3>자유 적립식</h3></v-tab>
            <v-tab class="ibm-plex-sans-kr-regular" @click="loaddata_period()"><h3>정액 적립식</h3></v-tab>
          </v-tabs>
        </v-col>
        <v-col class="d-flex justify-end">
          <v-select class="ps-16 ms-16 ibm-plex-sans-kr-regular" v-model="bank" :items="savingStore.bankList" label="은행" variant="outlined"></v-select>
        </v-col>
      </v-row>
    </v-container>
    <v-data-table-virtual height="600" :items="savingData" class="elevation-2" item-class="hoverable-row">
      <!-- userPeriod에 따라 다른 기간을 선택하여 표시 -->
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
      <template v-slot:item.상품명="{ item }">
        <v-btn class="mx-auto custom-btn" @click="showDetails(item.상품코드)">{{ item.상품명 }}</v-btn>
      </template>
    </v-data-table-virtual>

    <v-dialog v-model="dialog" width="1000">
      <SavingDetailComponent @close-dialog="dialog = false" />
    </v-dialog>
  </v-container>
</template>

<script setup>
import { onMounted, watch, ref } from "vue";
import { useSavingStore } from "@/stores/saving";
import { useUserStore } from "@/stores/user";
import SavingDetailComponent from "@/components/SavingDetailComponent.vue";

const userStore = useUserStore();
const dialog = ref(false);
const activeButton = ref("free");

const savingStore = useSavingStore();
const savingData = ref([]);
onMounted(() => {
  savingStore.getAllSaving();
});

const type = ref("");

// 자유 적립식
const loaddata_free = function () {
  let i = 1;
  activeButton.value = "free";
  if (savingStore.allSaving && savingStore.allSaving.length > 0) {
    savingData.value = savingStore.allSaving
      .map((element) => {
        const option6 = element.savingoption_set.find((option) => option.save_trm === 6 && option.rsrv_type_nm === "자유적립식");
        const intrRate6 = option6 ? option6.intr_rate : null;
        const option12 = element.savingoption_set.find((option) => option.save_trm === 12 && option.rsrv_type_nm === "자유적립식");
        const intrRate12 = option12 ? option12.intr_rate : null;
        const option24 = element.savingoption_set.find((option) => option.save_trm === 24 && option.rsrv_type_nm === "자유적립식");
        const intrRate24 = option24 ? option24.intr_rate : null;
        const option36 = element.savingoption_set.find((option) => option.save_trm === 36 && option.rsrv_type_nm === "자유적립식");
        const intrRate36 = option36 ? option36.intr_rate : null;

        // 모든 이자율 값이 null인지 확인
        if (intrRate6 === null && intrRate12 === null && intrRate24 === null && intrRate36 === null) {
          return null; // 모두 null이면 null을 반환
        }

        return {
          NO: i++,
          상품코드: element.fin_prdt_cd,
          은행: element.kor_co_nm,
          상품명: element.fin_prdt_nm,
          "6개월": intrRate6,
          "12개월": intrRate12,
          "24개월": intrRate24,
          "36개월": intrRate36,
        };
      })
      .filter((data) => data !== null); // null이 아닌 값만 필터링
  }
};

// 정기적립식
const loaddata_period = function () {
  let i = 1;
  activeButton.value = "period";
  if (savingStore.allSaving && savingStore.allSaving.length > 0) {
    savingData.value = savingStore.allSaving
      .map((element) => {
        const option6 = element.savingoption_set.find((option) => option.save_trm === 6 && option.rsrv_type_nm === "정액적립식");
        const intrRate6 = option6 ? option6.intr_rate : null;
        const option12 = element.savingoption_set.find((option) => option.save_trm === 12 && option.rsrv_type_nm === "정액적립식");
        const intrRate12 = option12 ? option12.intr_rate : null;
        const option24 = element.savingoption_set.find((option) => option.save_trm === 24 && option.rsrv_type_nm === "정액적립식");
        const intrRate24 = option24 ? option24.intr_rate : null;
        const option36 = element.savingoption_set.find((option) => option.save_trm === 36 && option.rsrv_type_nm === "정액적립식");
        const intrRate36 = option36 ? option36.intr_rate : null;

        // 모든 이자율 값이 null인지 확인
        if (intrRate6 === null && intrRate12 === null && intrRate24 === null && intrRate36 === null) {
          return null; // 모두 null이면 null을 반환
        }

        return {
          NO: i++,
          상품코드: element.fin_prdt_cd,
          은행: element.kor_co_nm,
          상품명: element.fin_prdt_nm,
          "6개월": intrRate6,
          "12개월": intrRate12,
          "24개월": intrRate24,
          "36개월": intrRate36,
        };
      })
      .filter((data) => data !== null); // null이 아닌 값만 필터링
  }
};

const bank = ref("은행을 선택해 보세요!");

watch(
  () => savingStore.allSaving,
  () => {
    if (type.value == 0) {
      bank.value = "모든은행";
      // 자유 적금
      loaddata_free();
    } else if (type.value == 1) {
      bank.value = "모든은행";
      // 정기 적금
      loaddata_period();
    }
  },
  { immediate: true }
);

watch(bank, () => {
  if (type.value == 0) {
    // 자유 적금
    loaddata_free();
  } else if (type.value == 1) {
    // 정기 적금
    loaddata_period();
  }
  if (bank.value !== "모든은행") {
    savingData.value = savingData.value.filter((item) => {
      return item.은행 === bank.value;
    });
  }
});

watch(type, () => {
  if (type.value == 0) {
    // 자유 적금
    loaddata_free();
  } else if (type.value == 1) {
    // 정기 적금
    loaddata_period();
  }
  if (bank.value !== "모든은행") {
    savingData.value = savingData.value.filter((item) => {
      return item.은행 === bank.value;
    });
  }
});

const showDetails = (productCode) => {
  findDetail(productCode);
  // 로딩 데이터 확인 후 출력될 다이얼로그 데이터에 삽입
  dialog.value = true;
};

const findDetail = function (productCode) {
  savingStore.getSavingData(productCode);
  savingStore.getSavingOptionData(productCode);
};

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
const userPeriod = userStore.userProfile.desirePeriod;
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
