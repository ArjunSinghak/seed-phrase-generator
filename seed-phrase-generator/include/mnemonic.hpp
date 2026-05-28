#ifndef MNEMONIC_HPP
#define MNEMONIC_HPP

#include <string>
#include <vector>
#include <cstdint>

namespace seed {

std::string to_mnemonic(const std::vector<uint8_t>& entropy);

} // namespace seed

#endif // MNEMONIC_HPP