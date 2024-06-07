<template>
  <div v-if="isLoading" class="loading-screen">
    <v-container fill-height align="center" justify="center">
      <v-progress-circular :model-value="value" :rotate="360" :size="100" :width="15" color="amber">
        <template v-slot:default>{{ value }} %</template>
      </v-progress-circular>
    </v-container>
  </div>
  <v-container v-else v-if="userProfile">
    <v-card class="mx-auto py-5">
      <v-row>
        <v-col class="my-auto" cols="6">
          <!-- 사용자 프로필 섹션 -->
          <ProfileUserInfoComponent :userProfile="userProfile" :profileImg="profileImg" />
          <v-card-actions>
            <v-container class="py-0 my-0 text-center">
              <v-dialog v-model="dialog" max-width="600" @click:outside="preventClose" persistent>
                <template v-slot:activator="{ props: activatorProps }">
                  <v-btn v-bind="activatorProps" color="yellow-darken-3" prepend-icon="mdi-account" variant="tonal" text="Edit Profile"></v-btn>
                </template>
                <ProfileUserEditComponent @close-dialog="dialog = false" />
              </v-dialog>
            </v-container>
          </v-card-actions>
          <v-col class="text-center">
            <ProfileUserChipComponent :userProfile="userProfile" />
          </v-col>
        </v-col>
        <!-- 예금 섹션 -->
        <v-col class="px-0 mx-0" cols="6">
          <v-row class="px-0 mx-0">
            <ProfileUserDepositComponent />
          </v-row>
          <!-- 적금 섹션 -->
          <v-row class="px-0 mx-0">
            <ProfileUserSavingComponent />
          </v-row>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>
<script setup>
import { ref, computed, onMounted } from "vue";
import { storeToRefs } from "pinia";
import { useUserStore } from "@/stores/user";
import { useDepositStore } from "@/stores/deposit";
import { useSavingStore } from "@/stores/saving";
import swal from "sweetalert";
import ProfileUserDepositComponent from "@/components/ProfileUserDepositComponent.vue";
import ProfileUserSavingComponent from "@/components/ProfileUserSavingComponent.vue";
import ProfileUserInfoComponent from "@/components/ProfileUserInfoComponent.vue";
import ProfileUserEditComponent from "@/components/ProfileUserEditComponent.vue";
import ProfileUserChipComponent from "@/components/ProfileUserChipComponent.vue";

const depositStore = useDepositStore();
const savingStore = useSavingStore();
const userStore = useUserStore();

const { userProfile } = storeToRefs(userStore);

const isLoading = ref(true);
const value = ref(0);
const interval = ref(-1);

onMounted(() => {
  userStore.getProfile();
  checkDeposit();
  checkSaving();
  // 프로그레스 서클 업데이트
  interval.value = setInterval(() => {
    if (value.value === 100) {
      value.value = 100;
    } else {
      value.value += 10;
    }
  }, 200);
  setTimeout(() => {
    isLoading.value = false;
    clearInterval(interval.value);
  }, 2000);
});

// 꿀바른 상품 확인 함수
const checkDeposit = function () {
  depositStore.getProfileDeposit(userProfile.value.interest_deposit);
};

const checkSaving = function () {
  savingStore.getProfileSaving(userProfile.value.interest_saving);
};

const dialog = ref(false);

const profileImg = computed(() => {
  return `http://localhost:8000${userProfile.value.profile_img}`;
});

const preventClose = function () {
  swal("Save 버튼을 눌러주세요!");
};
</script>

<style scoped>
.loading-screen {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  font-size: 24px;
}
</style>
