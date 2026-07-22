# Metric — AUT934129MAX / Prime / NP Contest Profile

Machine used: `AUD-PUBLIC-MACHINE-B` / `Prime` / `NP`
Scope mode: `scope-needs-review`

Source repo: `incjanta/metric`
Wrapper HEAD: `841950e39e2cfbaf4f9ae5d615f742e35817e4c5`
Direct target count: `79`
Contest: Sherlock Metric Contest — 150,000 USDC

## Active blockers carried forward

- SC-PROV-001: severity/rules provenance needs review.
- SC-KNOWN-001: prior-art duplicate gate needs review.
- SC-DEP-002: build/proof environment needs review.

## Scope files

- `metric-core/contracts/interfaces/callbacks/IMetricOmmModifyLiquidityCallback.sol`
- `metric-core/contracts/interfaces/callbacks/IMetricOmmSwapCallback.sol`
- `metric-core/contracts/interfaces/extensions/IMetricOmmExtensions.sol`
- `metric-core/contracts/interfaces/IExtsload.sol`
- `metric-core/contracts/interfaces/IMetricOmmPoolFactory/IMetricOmmPoolFactoryOwner.sol`
- `metric-core/contracts/interfaces/IMetricOmmPoolFactory/IMetricOmmPoolFactoryPoolAdmin.sol`
- `metric-core/contracts/interfaces/IMetricOmmPoolFactory/IMetricOmmPoolFactory.sol`
- `metric-core/contracts/interfaces/IMetricOmmPool/IMetricOmmPoolActions.sol`
- `metric-core/contracts/interfaces/IMetricOmmPool/IMetricOmmPoolCollectFees.sol`
- `metric-core/contracts/interfaces/IMetricOmmPool/IMetricOmmPoolFactoryActions.sol`
- `metric-core/contracts/interfaces/IMetricOmmPool/IMetricOmmPool.sol`
- `metric-core/contracts/interfaces/IPriceProvider/IPriceProvider.sol`
- `metric-core/contracts/libraries/BinDataLibrary.sol`
- `metric-core/contracts/libraries/CallExtension.sol`
- `metric-core/contracts/libraries/LiquidityLib.sol`
- `metric-core/contracts/libraries/PoolActions.sol`
- `metric-core/contracts/libraries/PoolStateLibrary.sol`
- `metric-core/contracts/libraries/SignedMath.sol`
- `metric-core/contracts/libraries/Slot0Library.sol`
- `metric-core/contracts/libraries/SwapMath.sol`
- `metric-core/contracts/libraries/ValidateExtensionsConfig.sol`
- `metric-core/contracts/MetricOmmPoolDeployer.sol`
- `metric-core/contracts/MetricOmmPoolFactory.sol`
- `metric-core/contracts/MetricOmmPool.sol`
- `metric-core/contracts/types/FactoryOperation.sol`
- `metric-core/contracts/types/FactoryStorage.sol`
- `metric-core/contracts/types/PoolExtensionsConfig.sol`
- `metric-core/contracts/types/PoolOperation.sol`
- `metric-core/contracts/types/PoolStorage.sol`
- `metric-core/contracts/types/Slot0.sol`
- `metric-core/contracts/utils/MetricReentrancyGuardTransient.sol`
- `metric-periphery/contracts/base/MetricOmmSwapRouterBase.sol`
- `metric-periphery/contracts/base/PeripheryPayments.sol`
- `metric-periphery/contracts/base/SelfPermit.sol`
- `metric-periphery/contracts/common/MetricOmmPoolStateView.sol`
- `metric-periphery/contracts/extensions/base/BaseMetricExtension.sol`
- `metric-periphery/contracts/extensions/DepositAllowlistExtension.sol`
- `metric-periphery/contracts/extensions/OracleValueStopLossExtension.sol`
- `metric-periphery/contracts/extensions/PriceVelocityGuardExtension.sol`
- `metric-periphery/contracts/extensions/SwapAllowlistExtension.sol`
- `metric-periphery/contracts/interfaces/extensions/IDepositAllowlistExtension.sol`
- `metric-periphery/contracts/interfaces/extensions/IOracleValueStopLossExtension.sol`
- `metric-periphery/contracts/interfaces/extensions/IPriceVelocityGuardExtension.sol`
- `metric-periphery/contracts/interfaces/extensions/ISwapAllowlistExtension.sol`
- `metric-periphery/contracts/interfaces/external/IERC20PermitAllowed.sol`
- `metric-periphery/contracts/interfaces/IMetricOmmPoolLiquidityAdder.sol`
- `metric-periphery/contracts/interfaces/IMetricOmmSimpleRouter.sol`
- `metric-periphery/contracts/interfaces/IMetricOmmSwapQuoter.sol`
- `metric-periphery/contracts/interfaces/IMulticall.sol`
- `metric-periphery/contracts/interfaces/IPeripheryPayments.sol`
- `metric-periphery/contracts/interfaces/ISelfPermit.sol`
- `metric-periphery/contracts/interfaces/IWETH9.sol`
- `metric-periphery/contracts/libraries/MetricOmmSwapInputs.sol`
- `metric-periphery/contracts/libraries/MetricOmmSwapPath.sol`
- `metric-periphery/contracts/libraries/MetricOmmSwapQuoteDecode.sol`
- `metric-periphery/contracts/libraries/MetricOmmSwapResults.sol`
- `metric-periphery/contracts/libraries/TransientCallbackPool.sol`
- `metric-periphery/contracts/MetricOmmPoolLiquidityAdder.sol`
- `metric-periphery/contracts/MetricOmmSimpleRouter.sol`
- `smart-contracts-poc/contracts/AnchoredPriceProvider.sol`
- `smart-contracts-poc/contracts/AnchoredProviderFactory.sol`
- `smart-contracts-poc/contracts/interfaces/IAnchoredProviderFactory.sol`
- `smart-contracts-poc/contracts/interfaces/IAnchorSource.sol`
- `smart-contracts-poc/contracts/interfaces/ICompressedOracleV1.sol`
- `smart-contracts-poc/contracts/oracles/compressed/CompressedOracle.sol`
- `smart-contracts-poc/contracts/oracles/compressed/OracleBase.sol`
- `smart-contracts-poc/contracts/oracles/providers/ChainlinkOracle.sol`
- `smart-contracts-poc/contracts/oracles/providers/docs/en/abuse-protection-integration.md`
- `smart-contracts-poc/contracts/oracles/providers/docs/ru/abuse-protection-integration.md`
- `smart-contracts-poc/contracts/oracles/providers/OracleBase.sol`
- `smart-contracts-poc/contracts/oracles/providers/PythOracle.sol`
- `smart-contracts-poc/contracts/oracles/utils/Codebook256.sol`
- `smart-contracts-poc/contracts/oracles/utils/LazerConsumer.sol`
- `smart-contracts-poc/contracts/oracles/utils/TimeMs.sol`
- `smart-contracts-poc/contracts/oracles/utils/U64x32.sol`
- `smart-contracts-poc/contracts/PriceProviderFactory.sol`
- `smart-contracts-poc/contracts/PriceProvider.sol`
- `smart-contracts-poc/contracts/ProtectedPriceProviderL2.sol`
- `smart-contracts-poc/contracts/ProtectedPriceProvider.sol`

Setup repo count: `10`
