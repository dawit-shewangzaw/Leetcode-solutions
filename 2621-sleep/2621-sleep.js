/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */
function sleep(millis) {
  return new Promise((resolve) => setTimeout(resolve, millis));
}