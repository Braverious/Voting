def get_voting_options():
    options = []
    options.append(input("Masukkan opsi voting pertama: "))
    options.append(input("Masukkan opsi voting kedua: "))
    
    while True:
        tambah_opsi = input("Ingin menambahkan opsi lain? (Y/N): ").strip().upper()
        if tambah_opsi == 'Y':
            opsi_baru = input("Masukkan opsi voting tambahan: ")
            options.append(opsi_baru)
        elif tambah_opsi == 'N':
            break
        else:
            print("Input tidak valid, silakan masukkan 'Y' atau 'N'.")
    return options


def get_voting_mode():
    while True:
        mode = input("Apakah voting tanpa batas maksimum pemilih? (Y untuk tanpa batas, N untuk jumlah tetap): ").strip().upper()
        if mode == 'Y':
            return None
        elif mode == 'N':
            while True:
                try:
                    max_voters = int(input("Masukkan jumlah maksimum pemilih: "))
                    if max_voters > 0:
                        return max_voters
                    else:
                        print("Jumlah pemilih harus lebih dari 0.")
                except ValueError:
                    print("Masukkan angka yang valid.")
        else:
            print("Input tidak valid, silakan masukkan 'Y' atau 'N'.")


def run_voting(options, max_voters=None):
    vote_counts = {option: 0 for option in options}
    voter_count = 0

    while True:
        print(f"\nJumlah voting masuk: {voter_count}" + (f"/{max_voters}" if max_voters else ""))
        print("\nOpsi Voting:")
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")

        try:
            choice = int(input("Pilih nomor opsi yang ingin Anda vote: "))
            if 1 <= choice <= len(options):
                vote_counts[options[choice - 1]] += 1
                voter_count += 1
            else:
                print("Pilihan tidak valid.")
                continue
        except ValueError:
            print("Masukkan angka yang valid.")
            continue
        
        if max_voters:
            if voter_count >= max_voters:
                break
        else:
            lanjut = input("Ingin melanjutkan voting? (Y/N): ").strip().upper()
            if lanjut != 'Y':
                break
    if max_voters:
        print(f"\nJumlah voting masuk: {voter_count}/{max_voters}")

    return vote_counts


def show_results(vote_counts):
    print("\nHasil Voting:")
    for option, count in vote_counts.items():
        print(f"{option}: {count} suara")


def main():
    print("=== Program Voting ===")
    options = get_voting_options()
    max_voters = get_voting_mode()
    results = run_voting(options, max_voters)
    show_results(results)


if __name__ == "__main__":
    main()
