# False Positive Reduction Example

## Initial Alert

Brute force detection triggered 50 alerts per day.

## Root Cause

- Service accounts retrying authentication
- Internal vulnerability scan IP generating failures

## Tuning Applied

- Excluded service accounts
- Whitelisted internal scanner IP
- Added time threshold condition

## Result

Alert volume reduced from 50 → 8 per day.

## Impact

Improved analyst efficiency and reduced noise.
