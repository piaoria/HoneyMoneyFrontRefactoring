<template>
  <v-card class="mx-auto" width="1000">
    <template v-slot:title>
      <v-row class="mb-0">
        <v-img :src="bankIcon" class="mt-10 ms-3" style="height: 40px; width: 30px"></v-img>
        <v-col class="pb-0 mt-6" cols="10">
          <span class="font-weight-black text-h5">{{ savingStore.getSavingDetail.fin_prdt_nm }}</span>
          <v-card-subtitle>{{ savingStore.getSavingDetail.kor_co_nm }} ({{ savingStore.getSavingDetail.dcls_month }})</v-card-subtitle>
        </v-col>
        <!-- 꿀바르기 버튼 시작-->
        <v-col class="py-0 my-0">
          <v-card-actions v-if="savingStore.getSavingDetail.interest_user && !savingStore.getSavingDetail.interest_user.includes(userStore.userInfo.id)" class="mt-3">
            <div>
              <v-img @click="saveEvent(savingStore.getSavingDetail.fin_prdt_cd, savingStore.getSavingDetail)" :src="empty" class="button-image hover-effect" style="width: 50px" />
              <div class="pe-2" align="center">{{ savingStore.getSavingDetail.interest_user?.length }}</div>
            </div>
          </v-card-actions>
          <v-card-actions v-else class="mt-3">
            <div>
              <v-img @click="deleteEvent(savingStore.getSavingDetail.fin_prdt_cd, savingStore.getSavingDetail)" :src="jar" class="button-image hover-effect" style="width: 50px" />
              <div class="pe-2" align="center">{{ savingStore.getSavingDetail.interest_user?.length }}</div>
            </div>
          </v-card-actions>
        </v-col>
        <!-- 꿀 바르기 버튼 끝 -->
      </v-row>
    </template>
    <hr />
    <v-row justify="center" align="center">
      <v-col cols="3" class="d-flex justify-center">
        <v-card-text class="text-style" align="center">가입 방법</v-card-text>
      </v-col>
      <v-col>
        <v-card-text class="">{{ savingStore.getSavingDetail.join_way }}</v-card-text>
      </v-col>
    </v-row>
    <hr />

    <v-row justify="center" align="center">
      <v-col cols="3" class="d-flex justify-center">
        <v-card-text class="text-style" align="center">만기 후 이자율</v-card-text>
      </v-col>
      <v-col>
        <v-card-text class="me-12">{{ savingStore.getSavingDetail.mtrt_int }}</v-card-text>
      </v-col>
    </v-row>
    <hr />
    <v-row justify="center" align="center">
      <v-col cols="3" class="d-flex justify-center">
        <v-card-text class="text-style" align="center">우대 조건</v-card-text>
      </v-col>
      <v-col>
        <v-card-text class="me-12">{{ savingStore.getSavingDetail.spcl_cnd }}</v-card-text>
      </v-col>
    </v-row>
    <hr />
    <v-row justify="center" align="center">
      <v-col cols="3" class="d-flex justify-center">
        <v-card-text class="text-style" align="center">가입 대상</v-card-text>
      </v-col>
      <v-col>
        <v-card-text class="">{{ savingStore.getSavingDetail.join_member }}</v-card-text>
      </v-col>
    </v-row>
    <hr />
    <v-row justify="center" align="center">
      <v-col cols="3" class="d-flex justify-center">
        <v-card-text class="text-style" align="center">가입 제한</v-card-text>
      </v-col>
      <v-col>
        <v-card-text class="">
          {{ savingStore.getSavingDetail.join_deny == 1 ? "제한없음" : savingStore.getSavingDetail.join_deny == 2 ? "서민전용" : savingStore.getSavingDetail.join_deny == 3 ? "일부제한" : "기타" }}
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
            savingStore.getSavingDetail.max_limit === null
              ? "한도 없음"
              : `${new Intl.NumberFormat("ko-KR", {
                  style: "currency",
                  currency: "KRW",
                }).format(savingStore.getSavingDetail.max_limit)}`
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
        <v-card-text class="me-12">{{ savingStore.getSavingDetail.etc_note }}</v-card-text>
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
import { useUserStore } from "@/stores/user";
import bankIcon from "@/assets/bank-icon.png";
import swal from "sweetalert";
import jar from "@/assets/jar.png";
import empty from "@/assets/empty.png";
import ChartComponent from "@/components/SavingChartComponent.vue";
import { defineEmits } from "vue";

const emit = defineEmits(["close-dialog"]);
const savingStore = useSavingStore();
const userStore = useUserStore();

const saveEvent = function (productCode, productInfo) {
  console.log(`꿀바르기!`);
  // 적금 쪽 확인
  swal("꿀통에 저장했습니다!", "PROFILE에서 꿀통을 확인하세요!", "success", {
    button: false,
    timer: 1500,
  });
  savingStore.getHoney(productCode);
  // 추가 토글
  savingStore.toggleData(productInfo);
};

const deleteEvent = function (productCode, productInfo) {
  console.log(`꿀버리기...`);
  // 적금 쪽 확인
  swal("꿀통에서 제거했습니다", "꿀통이 가벼워졌어요", "info", {
    button: false,
    timer: 1500,
  });
  savingStore.getHoney(productCode);
  // 제거 토글
  savingStore.toggleData(productInfo);
};

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
.btn-style {
  font-size: large;
  background-color: rgba(255, 174, 0, 0.661);
  border-radius: 5%px;
}
.custom-btn {
  background-color: #f5f5f5;
  box-shadow: none;
}

.custom-btn:hover {
  background-color: #f0f0f0; /* 마우스를 올렸을 때 연한 회색 배경색으로 변경 */
}

.button-image {
  transition: transform 0.3s, filter 0.3s;
  cursor: pointer;
}

.hover-effect:hover {
  transform: scale(1.2);
  filter: brightness(1.1);
}
</style>
