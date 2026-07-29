// Endpoint descriptor map: one entry per operationId in openapi/beli.yaml.
//
// `kind`:
//   - "read"             GET operations. Live-tested read-only; safe to call at will.
//   - "write-reversible"  POST/PUT operations that create state AND can be fully undone
//                          via `revert`. Live-tested: call, assert, then revert.
//   - "write-mock"        Every other POST/PUT operation. NOT live-tested against the
//                          real backend (would create un-revertable state, mutate a
//                          singleton the account depends on, or is itself the revert-half
//                          of a reversible flow above). Contract-checked only (shape of
//                          request/response validated against the OpenAPI schema).
//
// `Ctx` is defined here (not imported from ./runner) so this module has no dependency on
// Task 13's runner.ts. Task 13 should import `Ctx` FROM this module instead.
//
// The `revert` closures below invoke the generated SDK's flat, operationId-named exports
// directly (the same package Task 13's runner.ts dogfoods — see
// `sdks/typescript/src/sdk.gen.ts`), NOT a namespaced `ctx.sdk.<group>.<fn>()` shape (the
// package has no such namespacing). `Ctx.sdk` is the bearer-authenticated `Client` instance
// (built by `makeAuthedClient` in runner.ts), passed as the `client` option on each call —
// exactly as `runner.ts#runOps` does for reads.
import { updateFollow, deleteRanking, removeBookmark } from "beli-api-ts";

export type Ctx = {
  /** Bearer-authenticated SDK client for the logged-in test account. */
  sdk: any;
  /** UUID of the logged-in test user (the account the harness authenticates as). */
  userId: string;
  /** UUID of a second, distinct user usable as the target of follow/corr/etc. calls. */
  testTargetUser: string;
  /** Business id usable as the target of ranking/bookmark/etc. calls. */
  testTargetBusiness: number;
};

export type Descriptor = {
  kind: "read" | "write-reversible" | "write-mock";
  args?: (c: Ctx) => any;
  revert?: (c: Ctx, res: any) => Promise<void>;
};

export const DESCRIPTORS: Record<string, Descriptor> = {
  // --- auth ---
  login: { kind: "write-mock" },
  refreshToken: { kind: "write-mock" },
  getLoggedIn: { kind: "read" },
  updateUser: { kind: "write-mock" },
  updateDevice: { kind: "write-mock" },

  // --- profile ---
  getAppRank: { kind: "read" },
  getCheckUserSettings: { kind: "read" },
  getCountRankedThisYear: { kind: "read" },
  getCreatorSubscribe: { kind: "read" },
  getDatauserinteger: { kind: "read" },
  getGlassfyConfig: { kind: "read" },
  getHasContacts: { kind: "read" },
  getInvitesFeatureProgress: { kind: "read" },
  getInvitesRemaining: { kind: "read" },
  getNumberParamsBeforeUser: { kind: "read" },
  getNumberParams: { kind: "read" },
  getProfileProgress: { kind: "read" },
  getSharesheetConfig: { kind: "read" },
  getTasteProfileConfig: { kind: "read" },
  getTextParamsBeforeUser: { kind: "read" },
  getTextParams: { kind: "read" },
  getTrigger: { kind: "read" },
  createUserSetting: { kind: "write-mock" },
  getUserSetting: { kind: "read" },
  getUserBio: { kind: "read" },
  getUserMember: { kind: "read" },
  getUserStreak: { kind: "read" },

  // --- search ---
  getAllCities: { kind: "read" },
  getBusinessLink: { kind: "read" },
  getBusiness: { kind: "read" },
  getCuisineAllCuisines: { kind: "read" },
  getCurrentCity: { kind: "read" },
  getFilterConfigs: { kind: "read" },
  createFilterList: { kind: "write-mock" },
  createFilterOptions: { kind: "write-mock" },
  getPopularInCity: { kind: "read" },
  getPublishedListCities: { kind: "read" },
  searchApp: { kind: "read", args: () => ({ term: "coffee", city: "New York, NY" }) },
  getTopCities: { kind: "read" },
  getTrending: { kind: "read" },

  // --- business ---
  getBookmarkStatus: { kind: "read" },
  getBusinessCountRated: { kind: "read" },
  getBusinessFriendText: { kind: "read" },
  getBusinessHistogramData: { kind: "read" },
  getBusinessLabels: { kind: "read" },
  getClosedatauserbusinessboolean: { kind: "read" },
  getCountuserbusinessoccasion: { kind: "read" },
  getDatabusinessfloatSparse: { kind: "read" },
  getDatauserbusinesstextSparse: { kind: "read" },
  getDishRec: { kind: "read" },
  getFriendsBookmarked: { kind: "read" },
  getRecScore: { kind: "read" },
  getScores: { kind: "read" },
  getStaticMapsUrl: { kind: "read" },
  getSuggestBusinessCuisine: { kind: "read" },
  getSuggestBusinessPrice: { kind: "read" },
  getTaggedUsersOnBusiness: { kind: "read" },
  getUserBusinessLabels: { kind: "read" },
  getUserBusinessPhoto: { kind: "read" },
  getUserBusinessPhotos: { kind: "read" },
  getVisitDatesOnBusiness: { kind: "read" },
  createDataUserBusinessText: { kind: "write-mock" },

  // --- social ---
  getCorr: { kind: "read" },
  getFollowCountFollowers: { kind: "read" },
  getFollowCountFollowing: { kind: "read" },
  getFollowRequests: { kind: "read" },
  getFollow: { kind: "read" },
  createFollow: {
    kind: "write-reversible",
    args: (c) => ({ follower: c.userId, followed: c.testTargetUser }),
    // `res` is the unwrapped `FollowEdge` returned by createFollow (i.e. the caller's
    // `{ data }`, not the whole `{ data, error, response }` RequestResult) — `res.id` is the
    // new follow-edge's numeric id, required by PUT /api/follow/{id}/.
    revert: async (c, res) => {
      await updateFollow({
        client: c.sdk,
        path: { id: res.id },
        body: { unfollow_dt: new Date().toISOString() },
        headers: { Origin: "https://localhost" },
        throwOnError: false,
      });
    },
  },
  // Revert-half of createFollow above; invoked via the closure, not live-tested standalone.
  updateFollow: { kind: "write-mock" },
  getFollowers: { kind: "read" },
  getFollowing: { kind: "read" },
  getUserTagSuggestions: { kind: "read" },
  getLeaderboard: { kind: "read" },
  getMutualBookmarks: { kind: "read" },
  createPassedUserCorr: { kind: "write-mock" },
  getPeopleYouMayKnowFull: { kind: "read" },
  getSharedMeals: { kind: "read" },
  getTaggedUsers: { kind: "read" },
  getUserActivitySubscriptions: { kind: "read" },
  createUserList: { kind: "write-mock" },
  getUserSearch: { kind: "read" },

  // --- ranking ---
  createRanking: {
    kind: "write-reversible",
    args: (c) => ({
      category: "RES",
      user_id: c.userId,
      business_id: c.testTargetBusiness,
    }),
    // `res` is the unwrapped `AddRankingResponse` returned by createRanking. `results` is
    // `x-beli-unverified` (typed as `{[key: string]: unknown}`), so `id` is read defensively.
    revert: async (c, res) => {
      await deleteRanking({
        client: c.sdk,
        path: { uuid: c.userId, id: (res.results as Record<string, any>).id },
        headers: { Origin: "https://localhost" },
        throwOnError: false,
      });
    },
  },
  checkSharePostRank: { kind: "write-mock" },
  // Revert-half of createRanking above; invoked via the closure, not live-tested standalone.
  deleteRanking: { kind: "write-mock" },
  getBookmark: { kind: "read" },
  getRanking: { kind: "read" },
  processAddRanking: { kind: "write-mock" },
  getScoreAverage: { kind: "read" },
  getUserFieldCountBookmarked: { kind: "read" },
  getUserFieldCountRank: { kind: "read" },
  createUserRecScores: { kind: "write-mock" },
  getUserScoresCached: { kind: "read" },
  getUserScores: { kind: "read" },
  createBookmark: {
    kind: "write-reversible",
    args: (c) => ({ user: c.userId, business: c.testTargetBusiness, category: "RES" }),
    // Both createBookmark's and removeBookmark's request/response bodies are
    // `x-beli-unverified` in the spec (typed as `{[key: string]: unknown}`) — the revert
    // doesn't depend on the create response shape at all, it just re-sends the same
    // user/business identity that add-bookmark used.
    revert: async (c) => {
      await removeBookmark({
        client: c.sdk,
        body: { user: c.userId, business: c.testTargetBusiness },
        headers: { Origin: "https://localhost" },
        throwOnError: false,
      });
    },
  },
  // Revert-half of createBookmark above; invoked via the closure, not live-tested standalone.
  removeBookmark: { kind: "write-mock" },

  // --- feed ---
  getAggFollowingNew: { kind: "read" },
  getFeedAlert: { kind: "read" },
  getFeedItemData: { kind: "read" },
  getNewsfeedCurrent: { kind: "read" },
  getNewsfeedData: { kind: "read" },
  getNewsfeedReaction: { kind: "read" },
  getNewsfeedUser: { kind: "read" },
  getProfileNewsfeedData: { kind: "read" },
  getSingleNotificationData: { kind: "read" },
  getYourNewsfeedData: { kind: "read" },
  getYourNewsfeedReaction: { kind: "read" },

  // --- lists ---
  getChallengeJoinConfig: { kind: "read" },
  createChallengeProgressShare: { kind: "write-mock" },
  getMyFeaturedListChallenges: { kind: "read" },
  getPlaylists: { kind: "read" },
  getPublishedListItemNew: { kind: "read" },
  getPublishedList: { kind: "read" },
  getPublishedListByUser: { kind: "read" },
  getShortList: { kind: "read" },
  getUserGuideItemsClose: { kind: "read" },
  getUserGuideItems: { kind: "read" },
  getUserGuide: { kind: "read" },
  createUserHscrollListsPlacement: { kind: "write-mock" },

  // --- notifications ---
  getAppNotification: { kind: "read" },
  getBannerNotification: { kind: "read" },
  getBlockedMe: { kind: "read" },
  getBlocked: { kind: "read" },
  getCountAppNotificationUnread: { kind: "read" },
  getMarkRead: { kind: "read" },
  getMuted: { kind: "read" },
  getNotificationCommentCount: { kind: "read" },
  getNotificationReaction: { kind: "read" },
  updateNotification: { kind: "write-mock" },
  getPopup: { kind: "read" },

  // --- reservations ---
  getAvailableReservations: { kind: "read" },
  getBusinessResBookedList: { kind: "read" },
  createBusinessesResAvailability: { kind: "write-mock" },
  getResPriorityData: { kind: "read" },
  getResReportIssueOptions: { kind: "read" },
  getReservationPosting: { kind: "read" },
  getReservationsClaimedToday: { kind: "read" },

  // --- payments ---
  getAppleMapsToken: { kind: "read" },
  getStripePaymentMethods: { kind: "read" },

  // --- telemetry ---
  createActivity: { kind: "write-mock" },
  createApiError: { kind: "write-mock" },
};
